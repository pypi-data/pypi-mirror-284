import pandas as pd

from tqdm import tqdm
from anova_analysis import anova_ftest
from cell_range_calculator import calculate_cell_wise_ranges


def compute_best_ranges_anova(images_data, grid_size=8, lower_range_end=20, upper_range_start=80, step_size=2):
    """Identifies the best lower and upper range combinations for each grid cell based on the highest F-test statistic.

    This function iterates over a grid, identifying the combination of lower and upper range parameters that maximizes
    the F-test statistic for each cell.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing calculated F-test statistics and values for different range combinations, with columns
        including 'row', 'column', 'lower_range', 'upper_range', 'lower_range_val', 'upper_range_val', and 'one_way_f'.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.
    output_csv : str, optional
        The path to the output CSV file where the results will be saved, by default 'best_ranges_anova.csv'.
    num_samples : int, optional
        The number of images to randomly sample for each label (0 and 1), by default 20. 
    
    Notes
    -----
    - The best combination is determined by the maximum F-test statistic within each cell. Any 'nan' value is replaced 
    with '-1'. This ensures that the idxmax() function can be applied.
    """
    data_with_ranges = calculate_cell_wise_ranges(images_data=images_data, grid_size=grid_size, lower_range_end=lower_range_end, upper_range_start=upper_range_start, step_size=step_size)

    anova_results = anova_ftest(data_with_ranges=data_with_ranges, grid_size=grid_size, lower_range_end=lower_range_end, upper_range_start=upper_range_start, step_size=step_size)

    anova_results['f_statistic'] = anova_results['f_statistic'].fillna(-1)

    results = []

    for row in tqdm(range(grid_size), desc="Computing Best Ranges Using ANOVA"):
        for column in range(grid_size):
            cell_data = anova_results[(anova_results['row'] == row) & (anova_results['column'] == column)]
            best_combination = cell_data.loc[cell_data['f_statistic'].idxmax()]
            best_upper_range = best_combination['upper_range']
            best_lower_range = best_combination['lower_range']
            best_upper_range_val = best_combination['upper_range_val']
            best_lower_range_val = best_combination['lower_range_val']

            results.append([
                row,
                column,
                best_lower_range,
                best_upper_range,
                best_lower_range_val,
                best_upper_range_val
            ])

    columns = [
        'row', 'column', 'best_lower_range', 'best_upper_range', 'best_lower_range_val', 'best_upper_range_val'
    ]
    result_df = pd.DataFrame(results, columns=columns)

    return result_df


def compute_best_ranges_minmax(images_data, grid_size=8):
    rows = range(grid_size)
    columns = range(grid_size)

    images_data_label_0 = images_data[images_data['label'] == 0]
    results = []
        
    for row in tqdm(rows, desc="Computing Best Ranges Using MinMax"):
        for column in columns:
            subset_0 = images_data_label_0.loc[
                (images_data_label_0['row'] == row) & (images_data_label_0['column'] == column), 
                'cell_pixel_avg'
            ].values
            
            best_lower_range_val = subset_0.min()
            best_upper_range_val = subset_0.max()
            
            results.append([
                row,
                column,
                best_lower_range_val,
                best_upper_range_val
            ])
    
    columns = [
        'row', 'column', 'best_lower_range_val', 'best_upper_range_val'
    ]
    result_df = pd.DataFrame(results, columns=columns)

    return result_df