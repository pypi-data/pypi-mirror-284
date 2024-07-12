import pandas as pd

from scipy.stats import f_oneway
from tqdm import tqdm


def anova_ftest(data_with_ranges, grid_size=8, lower_range_end=20, upper_range_start=80, step_size=2):
    """Calculates F-test statistics and p-values for each combination of parameters between two datasets.

    This function performs one-way ANOVA F-tests for each combination of cell position and candidate range (row, column, 
    lower range and upper range) on data from two labels, 0 and 1 (non-anomalous and anomalous), using the S statistic. The results including
    the F-test statistic for each combination, are saved to a CSV file.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing processed train data with candidate ranges. The DataFrame must include the columns 'image_name', 'row', 'column', 'lower_range', 
        'upper_range', 'lower_range_val', 'upper_range_val', 'cell_pixel_avg' and 'label'.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.
    output_csv : str, optional
        The path to the output CSV file where the results will be saved, by default 'anova_results.csv'.
    """
    rows = range(grid_size)
    columns = range(grid_size)
    lower_ranges = range(0, lower_range_end, step_size)
    upper_ranges = range(upper_range_start, 100, step_size)

    upper_deviation = data_with_ranges['upper_range_val'] - data_with_ranges['cell_pixel_avg']
    lower_deviation = data_with_ranges['lower_range_val'] - data_with_ranges['cell_pixel_avg']
    data_with_ranges['S'] = upper_deviation.abs() + lower_deviation.abs()

    df_label_0 = data_with_ranges[data_with_ranges['label'] == 0]
    df_label_1 = data_with_ranges[data_with_ranges['label'] == 1]

    results = []

    for row in tqdm(rows, desc="Performing One-way ANOVA F-test"):
        for column in columns:
            for lower_range in lower_ranges:
                for upper_range in upper_ranges:
                    subset_label_0 = df_label_0[(df_label_0['row'] == row) &
                                                (df_label_0['column'] == column) &
                                                (df_label_0['lower_range'] == lower_range) &
                                                (df_label_0['upper_range'] == upper_range)]
                    
                    subset_label_1 = df_label_1[(df_label_1['row'] == row) &
                                                (df_label_1['column'] == column) &
                                                (df_label_1['lower_range'] == lower_range) &
                                                (df_label_1['upper_range'] == upper_range)]
                    
                    data_label_0 = subset_label_0['S'].values
                    data_label_1 = subset_label_1['S'].values

                    f_statistic, _ = f_oneway(*[data_label_0, data_label_1])

                    results.append([
                        row, column, lower_range, upper_range,
                        subset_label_0['lower_range_val'].values[0],
                        subset_label_0['upper_range_val'].values[0],
                        f_statistic
                    ])

    columns = [
        'row', 'column', 'lower_range', 'upper_range',
        'lower_range_val', 'upper_range_val', 'f_statistic'
    ]
    result_df = pd.DataFrame(results, columns=columns)

    return result_df