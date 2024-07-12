from banker_projection_model.abstracted_packages import (
    furtheredge_pandas as pd,
)
from banker_projection_model.abstracted_packages import furtheredge_numpy as np
from dateutil.relativedelta import relativedelta
from datetime import datetime


def generate_model_points(policies, run_settings):

    # Initialize index, values lists and modelpoints DataFrame
    index_list = []
    values_dict = {}
    modelpoints = pd.DataFrame()
    pivot_config = run_settings["pivot_config"]

    policies = load_rename_policies_columns(policies, run_settings)

    # Iterate over dictionary items
    for col, agg_func in pivot_config.items():
        if (col not in policies.columns) and (agg_func != "NOT_USED"):
            print(
                f"Warning: '{col}' is not present in the Policies DataFrame."
            )
            continue

        if agg_func.startswith("USED_DIRECT"):
            index_list.append(col)
        elif agg_func.startswith("USED_AGG"):
            agg_type = agg_func.split("_")[2]
            values_dict[col] = agg_type.lower()

    # Construct pivot table if there are columns to pivot on
    if len(index_list) > 0:
        modelpoints = policies.pivot_table(
            index=index_list,
            values=list(values_dict.keys()),
            aggfunc=values_dict,
        ).reset_index()
    else:
        print("No valid columns found to create a pivot table.")

    modelpoints.insert(0, "mp_id", np.arange(1, len(modelpoints) + 1))

    return modelpoints


def load_rename_policies_columns(policies, run_settings):

    mapping_dict = run_settings["mapping_columns_names_policies"]

    policies_renamed_df = rename_columns(policies, mapping_dict)

    policies_renamed_df["projection_date"] = datetime.strptime(
        run_settings["projection_date"], "%d/%m/%Y"
    )

    policies_renamed_df["inception_year"] = policies_renamed_df[
        "inception_date"
    ].dt.year
    policies_renamed_df["duration_init_m"] = policies_renamed_df.apply(
        lambda row: calculate_months_difference(
            row["projection_date"], row["inception_date"]
        ),
        axis=1,
    )

    policies_renamed_df["maturity_init_m"] = policies_renamed_df.apply(
        lambda row: calculate_months_difference(
            row["maturity_date"], row["inception_date"]
        ),
        axis=1,
    )
    policies_renamed_df["inception_date"] = pd.to_datetime(
        policies_renamed_df["inception_date"]
    )

    inception_date_vector = policies_renamed_df["inception_date"]
    years_timedelta = pd.to_timedelta(
        policies_renamed_df["payment_duration_y"] * 365, unit="D"
    )

    temp_date_4 = (
        inception_date_vector + years_timedelta - pd.DateOffset(months=3)
    )
    temp_date_12 = (
        inception_date_vector + years_timedelta - pd.DateOffset(months=1)
    )
    temp_date_2 = (
        inception_date_vector + years_timedelta - pd.DateOffset(months=6)
    )
    temp_date_1 = (
        inception_date_vector + years_timedelta - pd.DateOffset(months=12)
    )

    policies_renamed_df["end_payment_date"] = inception_date_vector

    conditions = [
        policies_renamed_df["payment_mode"] == 4,
        policies_renamed_df["payment_mode"] == 12,
        policies_renamed_df["payment_mode"] == 2,
        policies_renamed_df["payment_mode"] == 1,
    ]
    choices = [temp_date_4, temp_date_12, temp_date_2, temp_date_1]

    policies_renamed_df["end_payment_date"] = np.select(
        conditions, choices, default=inception_date_vector
    )
    policies_renamed_df.drop(["projection_date"], axis=1, inplace=True)
    return policies_renamed_df


def rename_columns(dataframe, mapping_dict):
    renamed_columns = {v: k for k, v in mapping_dict.items()}
    dataframe_renamed = dataframe.rename(columns=renamed_columns)

    return dataframe_renamed


def calculate_months_difference(end_date, start_date):
    delta = relativedelta(end_date, start_date)
    total_months_difference = delta.years * 12 + delta.months
    if delta.days > 0:
        total_months_difference += 1
    return total_months_difference
