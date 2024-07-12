import os
import warnings
import cv2
import pandas as pd
import numpy as np

from tqdm import tqdm


def calculate_cell_average(image_path, label, grid_size=8):
    """Reads an image, divides it into a grid of cells, and calculates the average pixel value for each cell.

    This function reads the specified image in grayscale, divides it into a grid defined by `grid_size`, calculates the
    average pixel value for each cell, and returns the results in a list of dictionaries. Each dictionary contains the
    image name, cell position (row, column), average cell pixel value and image label.

    Parameters
    ----------
    image_path : str
        The path to the image file.
    label : int
        The label for the image: 1 for anomalous and 0 for non-anomalous images.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.

    Returns
    -------
    pd.DataFrame
        A DataFrame, each containing the following columns:
        - 'image_name' (str): The name of the image file.
        - 'row' (int): The row index of the cell in the grid.
        - 'column' (int): The column index of the cell in the grid.
        - 'cell_pixel_avg' (float): The average pixel value of the cell.
        - 'label' (int): The label for the image.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f'Image {image_path} cannot be read.')

    height, width = image.shape
    cell_height = height // grid_size
    cell_width = width // grid_size

    data = []
    for row in range(grid_size):
        for column in range(grid_size):
            y1 = row * cell_height
            y2 = (row + 1) * cell_height
            x1 = column * cell_width
            x2 = (column + 1) * cell_width

            cell = image[y1:y2, x1:x2]
            cell_pixel_avg = np.mean(cell)
            image_name = os.path.basename(image_path)

            data.append([
                image_name,
                row,
                column,
                cell_pixel_avg,
                label
            ])
    return data


def calculate_cell_average_per_batch(image_paths, label, grid_size=8, desc="Processing Images"):
    """Processes images by iterating through image paths, computing average pixel values of cells within each 
    image after superimposing a grid using the `calculate_cell_average` function.

    Parameters
    ----------
    image_paths : List[str]
        The paths of images to be processed.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image.
    label : int
        The label for the images: 1 for anomalous and 0 for non-anomalous images.
    desc : str, optional
        Description for the tqdm progress bar, by default "Processing Sampled Images".
    """
    data = []

    for image_path in tqdm(image_paths, desc=desc):
        image_data = calculate_cell_average(image_path=image_path, label=label, grid_size=grid_size)
        data.extend(image_data)

    columns = [
        'image_name', 'row', 'column', 'cell_pixel_avg', 'label'
    ]
    result_df = pd.DataFrame(data, columns=columns)

    return result_df


def process_images(non_anomalous_paths=None, anomalous_paths=None, grid_size=8):
    """Processes images by computing average pixel values of cells within each image after superimposing a grid.

    Parameters
    ----------
    non_anomalous_paths : List[str]
        The paths of non-anomalous images.
    anomalous_paths : List[str]
        The paths of anomalous images.
    grid_size : int
        The size of the grid used to divide each image, by default 8.
    """
    if non_anomalous_paths is None and anomalous_paths is None:
        warnings.warn("Both non_anomalous_folder_path and anomalous_folder_path are None.")
        return pd.DataFrame()

    non_anomalous_df = pd.DataFrame()
    anomalous_df = pd.DataFrame()

    if non_anomalous_paths:
        non_anomalous_df = calculate_cell_average_per_batch(
            image_paths=non_anomalous_paths, 
            grid_size=grid_size,
            label=0, 
            desc="Processing Non-Anomalous Images"
        )
    
    if anomalous_paths:
        anomalous_df = calculate_cell_average_per_batch(
            image_paths=anomalous_paths, 
            grid_size=grid_size,
            label=1, 
            desc="Processing Anomalous Images"
        )

    return pd.concat([non_anomalous_df, anomalous_df], ignore_index=True)