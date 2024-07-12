from banker_projection_model.abstracted_packages import (
    furtheredge_pandas as pd,
)


def aggregate_projected_quarterly_cohort_level(
    df, columns_group_by, columns_to_aggregate
):
    grouped_df = df.groupby(columns_group_by, as_index=False)[
        columns_to_aggregate
    ].sum()
    row_counts = (
        df.groupby(columns_group_by).size().reset_index(name="counted_rows")
    )
    result_df = pd.merge(grouped_df, row_counts, on=columns_group_by)

    return result_df
