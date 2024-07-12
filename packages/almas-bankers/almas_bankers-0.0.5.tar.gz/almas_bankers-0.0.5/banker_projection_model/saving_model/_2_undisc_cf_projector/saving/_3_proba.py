from banker_projection_model.abstracted_packages import furtheredge_numpy as np
from banker_projection_model.abstracted_packages import (
    furtheredge_pandas as pd,
)


def proba_calculation(merged_df):
    """
    Perform probability calculations for the given DataFrame by applying various
    calculation functions and adding new columns with the results.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy and financial data.

    Returns:
        pandas.DataFrame: DataFrame with additional columns calculated based on input data.
    """

    print("Proba calculation")

    merged_df["annual_mortality_death_rt"] = annual_mortality_rate_death(
        merged_df
    )

    merged_df["annual_mortality_or_rt"] = annual_mortality_rate_or(merged_df)

    merged_df["annual_mortality_adb_rt"] = annual_mortality_rate_adb(merged_df)

    merged_df["monthly_survival_death_rt"] = monthly_survival_death_rate(
        merged_df
    )

    merged_df["monthly_survival_or_rt"] = monthly_survival_or_rate(merged_df)

    merged_df["monthly_survival_adb_rt"] = monthly_survival_adb_rate(merged_df)

    merged_df["monthly_stay_rt"] = monthly_stay_rate(merged_df)

    merged_df["incremental_survival_rt"] = incremental_survival_rate(merged_df)

    merged_df["cumulative_survival_rt"] = cumulative_survival_rate(merged_df)

    return merged_df


def annual_mortality_rate_death(merged_df):
    """
    Calculate the annual mortality rate due to death for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing mortality rates due to death for each row.
    """

    return (
        merged_df["emf"]
        * merged_df["qx_am80_2+_rt"]
        * merged_df["inforce_ind"]
    )


def annual_mortality_rate_or(merged_df):
    """
    Calculate the annual OR (Other Riders) mortality rate for each row in the DataFrame by summing up
    various other rates.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing overall mortality rates for each row.
    """
    return (
        merged_df["adjusted_qx_ptd_acc_rt"]
        + merged_df["adjusted_qx_ptd_own_rt"]
        + merged_df["adjusted_qx_ci_rt"]
        + merged_df["adjusted_qx_death_pwd_rt"]
        + merged_df["adjusted_qx_ptd_pwd_rt"]
        + merged_df["adjusted_qx_wop_rt"]
    ) * 12


def annual_mortality_rate_adb(merged_df):
    """
    Calculate the annual mortality rate due to accidental death benefit (ADB) for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing mortality rates due to ADB for each row.
    """

    return merged_df["inforce_ind"] * merged_df["adjusted_qx_adb_rt"]


def monthly_survival_death_rate(merged_df):

    annual_mortality_death_rate = merged_df["annual_mortality_death_rt"]

    return (1 - annual_mortality_death_rate) ** (1 / 12)


def monthly_survival_or_rate(merged_df):

    annual_mortality_or_rate = merged_df["annual_mortality_or_rt"]

    return (1 - annual_mortality_or_rate) ** (1 / 12)


def monthly_survival_adb_rate(merged_df):

    annual_mortality_adb_rate = merged_df["annual_mortality_adb_rt"]

    return (1 - annual_mortality_adb_rate) ** (1 / 12)


def monthly_stay_rate(merged_df):

    annual_lapse_rate = merged_df["annual_lapse_rt"]

    return (1 - annual_lapse_rate) ** (1 / 12)


def incremental_survival_rate(merged_df):
    monthly_survival_death_rate = merged_df["monthly_survival_death_rt"]
    monthly_survival_or_rate = merged_df["monthly_survival_or_rt"]
    monthly_survival_adb_rate = merged_df["monthly_survival_adb_rt"]
    monthly_stay_rate = merged_df["monthly_stay_rt"]

    return (
        monthly_survival_death_rate
        * monthly_survival_or_rate
        * monthly_survival_adb_rate
        * monthly_stay_rate
    )


def cumulative_survival_rate(merged_df):

    merged_df["incremental_survival_prod"] = (
        merged_df.groupby("mp_id")["incremental_survival_rt"]
        .cumprod()
        .shift(1)
        .fillna(1)
    )

    merged_df["cumulative_survival_rt"] = 1
    first_indices = merged_df.groupby("mp_id").head(1).index

    merged_df.loc[first_indices, "cumulative_survival_rt"] = 1

    merged_df["cumulative_survival_rt"] = (
        merged_df.groupby("mp_id")["cumulative_survival_rt"].transform(
            "cumprod"
        )
        * merged_df["incremental_survival_prod"]
    )

    first_indices = merged_df.groupby("mp_id").head(1).index

    merged_df.loc[first_indices, "cumulative_survival_rt"] = 1

    return merged_df["cumulative_survival_rt"]
