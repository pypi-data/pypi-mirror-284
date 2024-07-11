from banker_projection_model.abstracted_packages import furtheredge_numpy as np
from banker_projection_model.abstracted_packages import (
    furtheredge_pandas as pd,
)
import gc


def reserve_calculation_apply(merged_df):
    """
    Perform reserve calculations on the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data,
            including columns necessary for reserve calculations.

    Returns:
        pandas.DataFrame: DataFrame with additional columns for reserve calculations.
    """
    print("Reserve calculation")

    merged_df["premium_alloc_amt"] = premium_allocation_amount_res(merged_df)

    merged_df = process_sar_death_sar_adb_fund_value_av_fund_value(merged_df)

    merged_df["fund1_interest_amt"] = fund1_interest_amount(merged_df)

    return merged_df


def premium_allocation_amount_res(merged_df):
    """
    Calculate the premium allocation amount for reserves.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing the premium allocation amount for reserves.
    """
    return merged_df["net_paid_premium_amt"]


def _sar_death_education(merged_df):

    merged_df["monthly_interest_rt"] = (1 + merged_df["interest_rt"]) ** (
        1 / 12
    ) - 1
    merged_df["discount_factor"] = 1 / (
        (1 + merged_df["monthly_interest_rt"]) ** (merged_df["proj_m"])
    )
    merged_df["product_value"] = (
        merged_df["paid_premium_amt"] * merged_df["discount_factor"]
    )

    merged_df = merged_df.iloc[::-1]
    grouped_data = merged_df.groupby("mp_id")
    merged_df["van"] = grouped_data["product_value"].cumsum()
    merged_df = merged_df.iloc[::-1]

    output_temp = pd.DataFrame()
    output_temp["shifted_col"] = (
        merged_df.groupby(["mp_id"])["van"].shift(-1).fillna(0)
    )
    gc.collect()
    return (
        output_temp["shifted_col"]
        * merged_df["inforce_ind"]
        / merged_df["discount_factor"]
    )


def _sar_death_other(row, previous_av_fund):
    sa_cov1_amt = row["sa_death_amt"]
    return (
        max(0, sa_cov1_amt - previous_av_fund - row["premium_alloc_amt"])
        * row["inforce_ind"]
    )


def _sar_adb_education(merged_df):
    return merged_df["sar_death_amt"].values


def _sar_adb_other(row, previous_av_fund):
    sa_adb_amt = row["sa_adb_amt"]
    return (
        max(0, sa_adb_amt - previous_av_fund - row["premium_alloc_amt"])
        * row["inforce_ind"]
    )


def _coi_death(merged_df):
    """
    Calculate Cost of Insurance (COI) for death.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing COI for death.
    """
    return (
        merged_df["sar_death_amt"].values
        * merged_df["adjusted_qx_death_rt"].values
    )


def _coi_other_riders(merged_df):
    """
    Calculate Cost of Insurance (COI) for other riders.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing COI for other riders.
    """
    return merged_df["sar_death_amt"].values * (
        merged_df["adjusted_qx_ptd_acc_rt"].values
        + merged_df["adjusted_qx_ptd_own_rt"].values
        + merged_df["adjusted_qx_ci_rt"].values
        + merged_df["adjusted_qx_death_pwd_rt"].values
        + merged_df["adjusted_qx_ptd_pwd_rt"].values
        + merged_df["adjusted_qx_wop_rt"].values
    )


def _coi_adb(merged_df):
    """
    Calculate Cost of Insurance (COI) for ADB.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing COI for ADB.
    """
    return (
        merged_df["sar_adb_amt"].values
        * merged_df["adjusted_qx_adb_rt"].values
    )


def process_education_case(group):
    fund_values = []
    av_fund = []
    fmf_amt = []
    prev_av_fund = []
    prev_av_fund_value = 0

    for index, row in group.iterrows():
        if row["proj_m"] == 0:
            fund_value = row["initial_fund1_av_amt"]
            prev_av_fund_value = fund_value
            fund_value = (
                row["premium_alloc_amt"]
                - row["coi_death_amt"]
                - row["coi_or_amt"]
                - row["coi_adb_amt"]
                + prev_av_fund_value
            ) * row["inforce_ind"]
            fmf_amt_value = (row["fmf_pc"] * fund_value) / 12

            av_fund_value = (fund_value - fmf_amt_value) * (
                1 + row["guaranteed_interest_rt"]
            ) ** (1 / 12)
        else:

            fund_value = (
                row["premium_alloc_amt"]
                - row["coi_death_amt"]
                - row["coi_or_amt"]
                - row["coi_adb_amt"]
                + prev_av_fund_value
            ) * row["inforce_ind"]
            fmf_amt_value = (row["fmf_pc"] * fund_value) / 12

            av_fund_value = (fund_value - fmf_amt_value) * (
                1 + row["guaranteed_interest_rt"]
            ) ** (1 / 12)

        fund_values.append(fund_value)
        av_fund.append(av_fund_value)
        fmf_amt.append(fmf_amt_value)
        prev_av_fund.append(prev_av_fund_value)
        prev_av_fund_value = av_fund_value

    group["fund1_value_amt"] = fund_values
    group["fund1_av_amt"] = av_fund
    group["fmf_amt"] = fmf_amt
    group["prev_fund1_av_amt"] = prev_av_fund
    return group


def process_other_case(group):
    fund_values = []
    av_fund = []
    sar_death_other = []
    sar_or_amt = []
    sar_adb_other = []
    coi_death_amt = []
    coi_or_amt = []
    coi_adb_amt = []
    fmf_amt = []
    prev_av_fund = []
    prev_av_fund_value = 0
    av_fund_value = 0
    sar_death_value = 0
    sar_or_amt_value = 0
    sar_adb_value = 0
    coi_death_amt_value = 0
    coi_or_amt_value = 0
    coi_adb_amt_value = 0
    fmf_amt_value = 0
    for index, row in group.iterrows():
        if row["proj_m"] == 0:
            fund_value = row["initial_fund1_av_amt"]
            prev_av_fund_value = fund_value
            sar_death_value = _sar_death_other(row, prev_av_fund_value)
            sar_or_amt_value = sar_death_value
            sar_adb_value = _sar_adb_other(row, prev_av_fund_value)
            coi_death_amt_value = sar_death_value * row["adjusted_qx_death_rt"]
            coi_or_amt_value = sar_or_amt_value * (
                row["adjusted_qx_ptd_acc_rt"]
                + row["adjusted_qx_ptd_own_rt"]
                + row["adjusted_qx_ci_rt"]
                + row["adjusted_qx_death_pwd_rt"]
                + row["adjusted_qx_ptd_pwd_rt"]
                + row["adjusted_qx_wop_rt"]
            )
            coi_adb_amt_value = sar_adb_value * row["adjusted_qx_adb_rt"]
            fund_value = (
                row["premium_alloc_amt"]
                - coi_death_amt_value
                - coi_or_amt_value
                - coi_adb_amt_value
                + prev_av_fund_value
            ) * row["inforce_ind"]
            fmf_amt_value = (row["fmf_pc"] * fund_value) / 12
            av_fund_value = (fund_value - fmf_amt_value) * (
                1 + row["guaranteed_interest_rt"]
            ) ** (1 / 12)

        else:
            sar_death_value = _sar_death_other(row, prev_av_fund_value)
            sar_or_amt_value = sar_death_value
            sar_adb_value = _sar_adb_other(row, prev_av_fund_value)
            coi_death_amt_value = sar_death_value * row["adjusted_qx_death_rt"]
            coi_or_amt_value = sar_or_amt_value * (
                row["adjusted_qx_ptd_acc_rt"]
                + row["adjusted_qx_ptd_own_rt"]
                + row["adjusted_qx_ci_rt"]
                + row["adjusted_qx_death_pwd_rt"]
                + row["adjusted_qx_ptd_pwd_rt"]
                + row["adjusted_qx_wop_rt"]
            )
            coi_adb_amt_value = sar_adb_value * row["adjusted_qx_adb_rt"]
            fund_value = (
                row["premium_alloc_amt"]
                - coi_death_amt_value
                - coi_or_amt_value
                - coi_adb_amt_value
                + prev_av_fund_value
            ) * row["inforce_ind"]
            fmf_amt_value = (row["fmf_pc"] * fund_value) / 12
            av_fund_value = (fund_value - fmf_amt_value) * (
                1 + row["guaranteed_interest_rt"]
            ) ** (1 / 12)

        fund_values.append(fund_value)
        av_fund.append(av_fund_value)
        sar_death_other.append(sar_death_value)
        sar_or_amt.append(sar_or_amt_value)
        sar_adb_other.append(sar_adb_value)
        coi_death_amt.append(coi_death_amt_value)
        coi_or_amt.append(coi_or_amt_value)
        coi_adb_amt.append(coi_adb_amt_value)
        fmf_amt.append(fmf_amt_value)
        prev_av_fund.append(prev_av_fund_value)

        prev_av_fund_value = av_fund_value

    group["fund1_value_amt"] = fund_values
    group["fund1_av_amt"] = av_fund
    group["sar_death_amt"] = sar_death_other
    group["sar_or_amt"] = sar_or_amt
    group["sar_adb_amt"] = sar_adb_other
    group["coi_death_amt"] = coi_death_amt
    group["coi_or_amt"] = coi_or_amt
    group["coi_adb_amt"] = coi_adb_amt
    group["fmf_amt"] = fmf_amt
    group["prev_fund1_av_amt"] = prev_av_fund

    return group


def process_sar_death_sar_adb_fund_value_av_fund_value(merged_df):
    df_education = merged_df[
        merged_df["plan_type"] == "Education"
    ].reset_index(drop=True)
    df_other = merged_df[merged_df["plan_type"] != "Education"].reset_index(
        drop=True
    )

    output_result_education = pd.DataFrame()
    output_result_other = pd.DataFrame()

    if not df_education.empty:
        df_education["sar_death_amt"] = _sar_death_education(df_education)
        df_education["sar_or_amt"] = df_education["sar_death_amt"]
        df_education["sar_adb_amt"] = _sar_adb_education(df_education)

        df_education["coi_death_amt"] = _coi_death(df_education)
        df_education["coi_or_amt"] = _coi_other_riders(df_education)
        df_education["coi_adb_amt"] = _coi_adb(df_education)
        output_result_education = (
            df_education.groupby("mp_id")
            .apply(process_education_case)
            .reset_index(drop=True)
        )

    if not df_other.empty:
        output_result_other = (
            df_other.groupby("mp_id")
            .apply(process_other_case)
            .reset_index(drop=True)
        )

    final_result = pd.concat(
        [output_result_education, output_result_other]
    ).reset_index(drop=True)
    return final_result


def fund1_interest_amount(merged_df):
    """
    Calculate interest.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing interest values.
    """
    return (
        merged_df["fund1_av_amt"].values - merged_df["fund1_value_amt"].values
    )
