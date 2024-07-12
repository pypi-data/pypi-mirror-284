from banker_projection_model.saving_model._2_undisc_cf_projector.saving._1_duration import (
    duration_calculation,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.saving._2_reserve import (
    reserve_calculation_apply,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.saving._3_proba import (
    proba_calculation,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.saving._4_prospective import (
    prospective_calculation,
)

from banker_projection_model.saving_model._2_undisc_cf_projector.saving.required_data_calculation import (
    required_columns_duration,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.saving.required_data_calculation import (
    required_columns_reserve,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.saving.required_data_calculation import (
    required_columns_proba,
)
from banker_projection_model.saving_model._2_undisc_cf_projector.saving.required_data_calculation import (
    required_columns_prospective,
)

from banker_projection_model.saving_model._2_undisc_cf_projector.validator_dfs import (
    check_columns_existence,
)


dict_functions_mapping = {
    "duration": duration_calculation,
    "reserve": reserve_calculation_apply,
    "proba": proba_calculation,
    "prospective": prospective_calculation,
}


def saving_module(output):

    not_found_columns = []

    not_found_columns, output = sub_module_process(
        output,
        required_columns_duration,
        not_found_columns,
        "duration",
    )
    not_found_columns, output = sub_module_process(
        output,
        required_columns_reserve,
        not_found_columns,
        "reserve",
    )
    not_found_columns, output = sub_module_process(
        output,
        required_columns_proba,
        not_found_columns,
        "proba",
    )
    not_found_columns, output = sub_module_process(
        output,
        required_columns_prospective,
        not_found_columns,
        "prospective",
    )

    return output, not_found_columns


def sub_module_process(
    merged_df,
    required_columns,
    not_found_columns,
    sub_module_name,
):
    validator, not_found_columns_process = check_columns_existence(
        merged_df, required_columns
    )

    if sub_module_name in dict_functions_mapping:
        if validator:
            merged_df = dict_functions_mapping[sub_module_name](merged_df)
            not_found_columns.append(
                {
                    "process_name": sub_module_name,
                    "columns_not_found": not_found_columns_process,
                }
            )
        else:
            not_found_columns.append(
                {
                    "process_name": sub_module_name,
                    "columns_not_found": not_found_columns_process,
                }
            )
    return not_found_columns, merged_df
