from banker_projection_model.abstracted_packages import (
    furtheredge_pandas as pd,
)
from datetime import datetime
from banker_projection_model.saving_model._1_input_data_manager.model_point_generator import (
    generate_model_points,
)
from banker_projection_model.saving_model._1_input_data_manager.merge_all_tables import (
    merge_all_dfs_police,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.run_saving import (
    saving_module,
)


def saving_model_process(
    run_settings,
    policies,
    ri_rates,
    product_table,
    tech_assumptions,
    mortality_table,
    chunk_size=-100,
    projection_points=700,
):

    model_points = generate_model_points(policies, run_settings)

    projection_date = datetime.strptime(
        run_settings["projection_date"], "%d/%m/%Y"
    )

    if chunk_size <= 0:
        output = merge_all_dfs_police(
            model_points,
            ri_rates,
            tech_assumptions,
            mortality_table,
            product_table,
            projection_date,
            projection_points,
        )
        result_df, not_found_columns = saving_module(output)

        return result_df, not_found_columns
    else:
        all_result_df = pd.DataFrame()

        for chunk_start in range(0, len(model_points), chunk_size):
            chunk_end = min(chunk_start + chunk_size, len(model_points))
            chunk_model_points = model_points[chunk_start:chunk_end]
            output = merge_all_dfs_police(
                chunk_model_points,
                ri_rates,
                tech_assumptions,
                mortality_table,
                product_table,
                projection_date,
                projection_points,
            )
            result_df, not_found_columns = saving_module(output)

            all_result_df = pd.concat(
                [all_result_df, result_df],
                ignore_index=True,
            )

        return all_result_df, not_found_columns
