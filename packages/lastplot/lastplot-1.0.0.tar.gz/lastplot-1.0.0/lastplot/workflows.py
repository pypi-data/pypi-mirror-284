from lastplot.computing_statistics import *
from lastplot.data_cleanup import *
from lastplot.saving import *


def data_workflow(file_path, data_sheet, mice_sheet, output_path, control_name):
    """
    Automatically processes lipidomics data.

    :param file_path: Path of the Excel file containing the data.
    :param data_sheet: Name of the sheet containing the data.
    :param mice_sheet: Name of the sheet containing the information about the subjects.
    :param output_path: Path of where to save the outputs.
    :param control_name: Name of the control subject group.
    """

    df, df_mice = load_data(datapath=file_path, sheet_name=data_sheet, mice_sheet=mice_sheet)
    df_clean = data_cleanup(df=df, df_mice=df_mice, output_path=output_path)
    statistics = statistics_tests(df_clean=df_clean, control_name=control_name)
    df_final = z_scores(df_clean=df_clean, statistics=statistics)
    save_values(df_final=df_final, output_path=output_path)
    save_zscores(df_final=df_final, output_path=output_path)

    return df_final
