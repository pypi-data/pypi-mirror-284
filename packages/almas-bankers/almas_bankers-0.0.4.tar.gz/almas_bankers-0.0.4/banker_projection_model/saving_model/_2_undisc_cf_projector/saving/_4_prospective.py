from banker_projection_model.abstracted_packages import furtheredge_numpy as np
from banker_projection_model.abstracted_packages import (
    furtheredge_pandas as pd,
)


def prospective_calculation(merged_df):
    """
    Perform prospective calculations for the given DataFrame by applying various
    calculation functions and adding new columns with the results.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy and financial data.

    Returns:
        pandas.DataFrame: DataFrame with additional columns calculated based on input data.
    """

    print("Prospective calculation")

    merged_df["lrc_premium_amt"] = lrc_premium_amount(merged_df)

    merged_df["lrc_commission_amt"] = commission_amount(merged_df)

    # Benefits amounts (Death & OR & ADB)

    merged_df["death_benefits_amt"] = death_benefits_amount(merged_df)

    merged_df["or_benefits_amt"] = or_benefits_amount(merged_df)

    merged_df["adb_benefits_amt"] = adb_benefits_amount(merged_df)

    # Claims amounts (Mortality & Surrender & Maturity)

    merged_df["mortality_claims_amt"] = mortality_claims_amount(merged_df)

    merged_df["surrender_claims_amt"] = surrender_claims_amount(merged_df)

    merged_df["maturity_claims_amt"] = maturity_claims_amount(merged_df)

    merged_df["lrc_claims_amt"] = lrc_claims_amount(merged_df)

    # Expense amounts

    merged_df["maintenance_expens_amt"] = maintenance_expenses_amount(
        merged_df
    )

    # Reinsurance amounts and rates

    merged_df["ceded_sa_amt"] = ceded_sum_assured(merged_df)

    merged_df["cession_rt"] = cession_rate(merged_df)

    merged_df["lrc_re_premium_amt"] = premium_paid_to_reinsurer(merged_df)

    merged_df["lrc_re_commission_amt"] = commission_received_from_reinsurer(
        merged_df
    )

    merged_df["lrc_re_claims_amt"] = claims_paid_by_reinsurer(merged_df)

    merged_df["lrc_re_profitsharing_amt"] = reinsurance_profit_sharing(
        merged_df
    )

    return merged_df


def lrc_premium_amount(merged_df):
    """
    Calculate premium prospects for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for premium prospect calculation.

    Returns:
        pandas.Series: Series containing the premium prospects for each row
        in the merged_df DataFrame.
    """

    paid_premium_amt = merged_df["paid_premium_amt"]
    cumulative_survival_rate = merged_df["cumulative_survival_rt"]
    inforce_ind = merged_df["inforce_ind"]

    lrc_premium_amount = (
        paid_premium_amt * cumulative_survival_rate * inforce_ind
    )

    return lrc_premium_amount


def commission_amount(merged_df):
    """
    Calculate the commission amount for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for commission calculation.

    Returns:
        pandas.Series: Series containing the commission amount for each row
        in the merged_df DataFrame.
    """

    commissions_pc = merged_df["commissions_pc"]

    commission_amount = merged_df["lrc_premium_amt"] * commissions_pc

    return commission_amount


def death_benefits_amount(merged_df):

    cumulative_survival_rate = merged_df["cumulative_survival_rt"]
    prev_fund1_av_amt = merged_df["prev_fund1_av_amt"]
    premium_alloc_amt = merged_df["premium_alloc_amt"]
    sar_death_amt = merged_df["sar_death_amt"]

    monthly_survival_death_rt = merged_df["monthly_survival_death_rt"]

    inforce_ind = merged_df["inforce_ind"]
    fundav_ind = merged_df["fundav_ind"]

    death_benefits_amount = (
        (prev_fund1_av_amt + premium_alloc_amt + sar_death_amt)
        * (1 - monthly_survival_death_rt)
        * inforce_ind
        * cumulative_survival_rate
        * fundav_ind
    )

    return death_benefits_amount


def or_benefits_amount(merged_df):

    cumulative_survival_rate = merged_df["cumulative_survival_rt"]
    prev_fund1_av_amt = merged_df["prev_fund1_av_amt"]
    premium_alloc_amt = merged_df["premium_alloc_amt"]

    monthly_survival_or_rt = merged_df["monthly_survival_or_rt"]

    inforce_ind = merged_df["inforce_ind"]
    fundav_ind = merged_df["fundav_ind"]

    or_benefits_amount = (
        (prev_fund1_av_amt + premium_alloc_amt)
        * (1 - monthly_survival_or_rt)
        * inforce_ind
        * cumulative_survival_rate
        * fundav_ind
    )

    return or_benefits_amount


def adb_benefits_amount(merged_df):

    cumulative_survival_rate = merged_df["cumulative_survival_rt"]
    sar_adb_amt = merged_df["sar_adb_amt"]

    inforce_ind = merged_df["inforce_ind"]
    fundav_ind = merged_df["fundav_ind"]

    monthly_survival_death_rt = merged_df["monthly_survival_death_rt"]
    monthly_survival_adb_rt = merged_df["monthly_survival_adb_rt"]

    adb_benefits_amount = (
        sar_adb_amt
        * (1 - monthly_survival_death_rt)
        * fundav_ind
        * inforce_ind
        * cumulative_survival_rate
        * (1 - monthly_survival_adb_rt)
    )

    return adb_benefits_amount


def mortality_claims_amount(merged_df):

    death_benefits_amt = merged_df["death_benefits_amt"]

    or_benefits_amt = merged_df["or_benefits_amt"]

    adb_benefits_amt = merged_df["adb_benefits_amt"]

    mortality_claims_amount = (
        death_benefits_amt + or_benefits_amt + adb_benefits_amt
    )

    return mortality_claims_amount


def surrender_claims_amount(merged_df):
    """
    Calculate surrender claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for surrender claim calculation.

    Returns:
        pandas.Series: Series containing the surrender claims for each row
        in the merged_df DataFrame.
    """
    prev_fund1_av_amt = merged_df["prev_fund1_av_amt"]
    cumulative_survival_rt = merged_df["cumulative_survival_rt"]
    monthly_stay_rt = merged_df["monthly_stay_rt"]
    inforce_id = merged_df["inforce_ind"]
    surrender_charge_pc = merged_df["surrender_charge_pc"]

    annual_mortality_death_rt = merged_df["annual_mortality_death_rt"]
    annual_mortality_or_rt = merged_df["annual_mortality_or_rt"]
    annual_mortality_adb_rt = merged_df["annual_mortality_adb_rt"]

    surr_claim_amt = (
        prev_fund1_av_amt
        * cumulative_survival_rt
        * (1 - monthly_stay_rt)
        * inforce_id
        * (1 - surrender_charge_pc)
        * (
            (
                1
                - annual_mortality_death_rt
                - annual_mortality_or_rt
                - annual_mortality_adb_rt
            )
            ** (1 / 12)
        )
    )

    return surr_claim_amt


def maturity_claims_amount(merged_df):

    maturity_claims = (
        np.where(
            merged_df["maturity_init_m"] == merged_df["proj_init_m"],
            merged_df["fund1_av_amt"],
            0,
        )
        * merged_df["incremental_survival_rt"]
        * merged_df["cumulative_survival_rt"]
    )

    return maturity_claims


def lrc_claims_amount(merged_df):

    mortality_claims_amount = merged_df["mortality_claims_amt"]

    surrender_claim_amount = merged_df["surrender_claims_amt"]

    maturity_claims_amount = merged_df["maturity_claims_amt"]

    return (
        mortality_claims_amount
        + surrender_claim_amount
        + maturity_claims_amount
    )


def maintenance_expenses_amount(merged_df):
    """
    Calculate maintenance expenses for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for maintenance expense calculation.

    Returns:
        pandas.Series: Series containing the maintenance expenses for each row
        in the merged_df DataFrame.
    """
    cumulative_survival_rt = merged_df["cumulative_survival_rt"]
    if_ind = merged_df["inforce_ind"]
    lrc_premium_amt = merged_df["lrc_premium_amt"]
    fixed_loading_amt = merged_df["fixed_loading_amt"]

    inflation_rt = merged_df["inflation_rt"]

    variable_loading_pc = merged_df["variable_loading_pc"]

    proj_y = (merged_df["proj_m"] // 12) + 1
    main_expens = (
        cumulative_survival_rt
        * fixed_loading_amt
        / 12
        * if_ind
        * (1 + inflation_rt) ** (proj_y - 1)
        + variable_loading_pc * lrc_premium_amt
    ) * if_ind
    return main_expens


def ceded_sum_assured(merged_df):
    """
    Calculate ceded sum assured for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for ceded sum assured calculation.

    Returns:
        pandas.Series: Series containing the ceded sum assured for each row
        in the merged_df DataFrame.
    """

    sa_death_amt = merged_df["sa_death_amt"]

    death_retention_amt = merged_df["death_retention_amt"]
    ceded_sa = np.maximum(sa_death_amt - death_retention_amt, 0)

    return ceded_sa


def cession_rate(merged_df):
    """
    Calculate cession rate for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for cession rate calculation.

    Returns:
        pandas.Series: Series containing the cession rate for each row
        in the merged_df DataFrame.
    """

    cess_rate = np.where(
        merged_df["sa_death_amt"] == 0,
        0,
        merged_df["ceded_sa_amt"] / merged_df["sa_death_amt"],
    )

    return cess_rate


def premium_paid_to_reinsurer(merged_df):
    """
    Calculate premium paid to reinsurer for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for premium paid to reinsurer calculation.

    Returns:
        pandas.Series: Series containing the premium paid to reinsurer for each row
        in the merged_df DataFrame.
    """
    cess_rate = merged_df["cession_rt"]

    coi_death = merged_df["coi_death_amt"]
    coi_or = merged_df["coi_or_amt"]
    coi_adb = merged_df["coi_adb_amt"]
    cumulative_survival_rt = merged_df["cumulative_survival_rt"]
    coi_pc = merged_df["coi_pc"]
    prem_reins = (
        cess_rate
        * (coi_death + coi_or + coi_adb)
        * cumulative_survival_rt
        / coi_pc
    )

    return prem_reins


def commission_received_from_reinsurer(merged_df):
    """
    Calculate commission received from reinsurer for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for commission received from reinsurer calculation.

    Returns:
        pandas.Series: Series containing the commission received from reinsurer for each row
        in the merged_df DataFrame.
    """
    ri_commission_pc = merged_df["ri_commission_pc"]
    lrc_re_premium_amt = merged_df["lrc_re_premium_amt"]

    commission_year = -ri_commission_pc * lrc_re_premium_amt
    condition_year = merged_df["proj_init_y"] == 1

    comiss_reins = commission_year * lrc_re_premium_amt * condition_year

    return comiss_reins


def claims_paid_by_reinsurer(merged_df):
    """
    Calculate claims paid by reinsurer for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for claims paid by reinsurer calculation.

    Returns:
        pandas.Series: Series containing the claims paid by reinsurer for each row
        in the merged_df DataFrame.
    """

    cess_rate = merged_df["cession_rt"]
    sar_death1 = merged_df["sar_death_amt"]
    sar_or = merged_df["sar_or_amt"]
    sar_adb = merged_df["sar_adb_amt"]

    monthly_survival_death_rt = merged_df["monthly_survival_death_rt"]
    monthly_survival_or_rt = merged_df["monthly_survival_or_rt"]
    monthly_survival_adb_rt = merged_df["monthly_survival_adb_rt"]

    cumulative_survival_rt = merged_df["cumulative_survival_rt"]
    if_ind = merged_df["inforce_ind"]
    emf = merged_df["emf"]
    claim_reins = (
        cess_rate
        * (
            sar_death1 * (1 - monthly_survival_death_rt)
            + sar_or * (1 - monthly_survival_or_rt)
            + sar_adb * (1 - monthly_survival_adb_rt)
        )
        * cumulative_survival_rt
        * if_ind
    ) / emf

    return claim_reins


def reinsurance_profit_sharing(merged_df):
    """
    Calculate reinsurance profit sharing for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for reinsurance profit sharing calculation.

    Returns:
        pandas.Series: Series containing the reinsurance profit sharing for each row
        in the merged_df DataFrame.
    """
    lrc_re_premium_amt = merged_df["lrc_re_premium_amt"]
    lrc_re_commission_amt = merged_df["lrc_re_commission_amt"]
    lrc_re_claims_amt = merged_df["lrc_re_claims_amt"]

    reins_prof_sharing = np.maximum(
        0.5
        * (1 - 0.15)
        * (-lrc_re_premium_amt)
        * lrc_re_commission_amt
        * lrc_re_claims_amt,
        0,
    )
    return reins_prof_sharing
