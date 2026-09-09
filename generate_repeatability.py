"""
This code is used to generate repeatability of a measurement using the standard error of 
measurement (SEM) and the minimal detectable change (MDC). The UCLA repeated measures exercise 
dataset is used for demonstration. The example data is read from a CSV file and the SEM and MDC are 
calculated using the pingouin library.
"""
import numpy as np
import pandas as pd
import pingouin as pg


def get_sem(df, subject_variable, measurement_variable, repetition_variable):
    """
    Compute the standard error of measurement (SEM) and minimal detectable change (MDC) from a 
    repeated measures ANOVA.
    """
    # compute repeated measures ANOVA
    rm_aov = pg.rm_anova(
        data=df,
        dv=measurement_variable,
        within=repetition_variable,
        subject=subject_variable,
        detailed=True
    )
    # extract MS error corresponding to the subject x repetition interaction/residual
    ms_error = rm_aov.loc[rm_aov['Source'] == 'Error', 'MS'].values[0]
    # store sem
    sem = np.sqrt(ms_error)
    # store mdc
    mdc = 1.96 * np.sqrt(2) * sem
    return sem, mdc


if __name__ == '__main__':

    # --- read data ---
    EXAMPLE_DATA_PATH = r'.\exer.csv'
    example_data_df = pd.read_csv(EXAMPLE_DATA_PATH)
    # obtain example data subset : (1) at rest, (2) walking leisurely or (3) running
    subset_data_df = example_data_df[example_data_df['exertype'] == 1]

    # --- variables setup ---
    # assign data-specific variables
    example_subject_variable = subset_data_df.columns.tolist()[0]
    example_measurement_variable = subset_data_df.columns.tolist()[3]
    example_repetition_variable = subset_data_df.columns.tolist()[4]

    # --- obtain repeatability ---
    sem_value, mdc_value = get_sem(subset_data_df,
                           example_subject_variable,
                           example_measurement_variable,
                           example_repetition_variable)

    # show results
    print(f"SEM: {sem_value:.3f} bpm\nMDC: {mdc_value:.3f} bpm")
