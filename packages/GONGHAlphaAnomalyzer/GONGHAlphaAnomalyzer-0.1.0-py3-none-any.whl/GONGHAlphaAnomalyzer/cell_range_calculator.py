import numpy as np
import pandas as pd

from tqdm import tqdm


def calculate_range_values(df, lower_range=2, upper_range=98):
    """Calculates the specified lower and upper percentile values for the 'cell_pixel_avg' column in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the 'cell_pixel_avg' column for which the percentiles will be calculated.
    lower_range : float, optional
       The lower percentile to calculate, by default 4.
    upper_range : float, optional
        The upper percentile to calculate, by default 96.

    Returns
    -------
    lower_range_val : float
        The value at the specified lower percentile for the 'cell_pixel_avg' column.
    upper_range_val : float
        The value at the specified upper percentile for the 'cell_pixel_avg' column.
   """
    lower_range_val = np.percentile(df['cell_pixel_avg'], lower_range)
    upper_range_val = np.percentile(df['cell_pixel_avg'], upper_range)

    return lower_range_val, upper_range_val


def calculate_cell_wise_ranges(images_data, grid_size=8, lower_range_end=20, upper_range_start=80, step_size=2):
    """calculate cell-wise candidate percntile ranges.

    This function filters a DataFrame of images labeled as 0 (non-anomalous) and 1 (anomalous) by their respective
    labels and calculates candidate percentile ranges for each cell in the images.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the image data, with columns 'image_name', 'row', 'column', 'cell_pixel_avg', and 
        'label'.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.
    num_samples : int, optional
        The number of images to randomly sample for each label (0 and 1), by default 20.

    Notes
    -----
    - The function uses a fixed random seed (123) for reproducible sampling.
    - Percentile ranges are calculated for lower percentiles from 0 to 18 and upper percentiles from 80 to 98, in steps 
    of 2.
    """
    all_ranges = []

    for image_name in tqdm(images_data['image_name'].unique(), desc="Writing Candidate Ranges"):
        image_data = images_data[images_data['image_name'] == image_name]

        for lower_range in range(0, lower_range_end, step_size):
            for upper_range in range(upper_range_start, 100, step_size):
                for row in range(grid_size):
                    for column in range(grid_size):
                        data_cells = images_data[
                            (images_data['row'] == row) &
                            (images_data['column'] == column)
                        ]

                        lower_range_val, upper_range_val = calculate_range_values(data_cells, lower_range, upper_range)
                        data_cell = image_data[
                            (image_data['row'] == row) &
                            (image_data['column'] == column)
                        ]

                        if not data_cell.empty:
                            all_ranges.append([
                                image_name, row, column, lower_range, upper_range,
                                lower_range_val, upper_range_val,
                                data_cell['cell_pixel_avg'].values[0],
                                data_cell['label'].values[0]
                            ])

    columns = [
        'image_name', 'row', 'column', 'lower_range', 'upper_range',
        'lower_range_val', 'upper_range_val', 'cell_pixel_avg', 'label'
    ]
    df_all_ranges  = pd.DataFrame(all_ranges, columns=columns)

    return df_all_ranges 