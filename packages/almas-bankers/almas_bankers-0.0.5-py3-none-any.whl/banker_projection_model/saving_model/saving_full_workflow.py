from banker_projection_model.saving_model.saving_model_proj import (
    saving_model_process,
)
from banker_projection_model.saving_model.quarterly_projected_result import (
    quarterly_projected_cohort_level,
)


def saving_model_workflow(
    run_settings,
    policies,
    ri_rates,
    product_table,
    tech_assumptions,
    mortality_table,
    chunk_size,
    list_projected_columns_agg_final,
    list_non_projected_columns_final,
    projection_points=1000,
):

    df_policy_level, not_found_columns = saving_model_process(
        run_settings,
        policies,
        ri_rates,
        product_table,
        tech_assumptions,
        mortality_table,
        chunk_size,
        projection_points,
    )
    non_proj_df_policy_level = (
        df_policy_level[list_non_projected_columns_final]
    ).drop_duplicates()
    df_quarterly_cohort_level = quarterly_projected_cohort_level(
        df_policy_level, list_projected_columns_agg_final
    )
    return (
        df_quarterly_cohort_level,
        non_proj_df_policy_level,
        not_found_columns,
    )
