from banker_projection_model.saving_model._1_input_data_manager.data_aggregate import (
    aggregate_projected_quarterly_cohort_level,
)


def extract_cohort(proj_date):
    year = proj_date.year
    quarter = (proj_date.month - 1) // 3 + 1
    return f"{year}Q{quarter}"


def quarterly_projected_cohort_level(
    df_monthly_policy_level, list_projected_columns_final
):

    df_monthly_policy_level["cohort"] = (
        "unitlink_"
        + df_monthly_policy_level["plan_type"]
        + "_"
        + df_monthly_policy_level["inception_year"]
    )

    df_monthly_policy_level["proj_quarter"] = df_monthly_policy_level[
        "proj_date"
    ].apply(extract_cohort)
    resulted_df_quarter_cohort_level = (
        aggregate_projected_quarterly_cohort_level(
            df_monthly_policy_level,
            ["cohort", "proj_quarter"],
            list_projected_columns_final,
        )
    )

    return resulted_df_quarter_cohort_level
