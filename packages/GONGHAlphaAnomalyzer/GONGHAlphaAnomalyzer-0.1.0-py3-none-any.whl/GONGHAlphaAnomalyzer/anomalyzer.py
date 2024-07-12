import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from matplotlib.colors import Normalize, to_rgba
from matplotlib.cm import ScalarMappable
from tqdm import tqdm
from PIL import Image
from plots_generator import sigmoid
from best_ranges_calculator import compute_best_ranges_anova, compute_best_ranges_minmax
from cell_average_calculator import process_images


class Anomalyzer:
    def __init__(self, grid_size: int = 8):
        self.grid_size = grid_size
        self.best_ranges: pd.DataFrame = pd.DataFrame()
        self.images_data: pd.DataFrame = pd.DataFrame()

    def compute_best_ranges(self,
                            non_anomalous_paths: [],
                            anomalous_paths: [],
                            method: str = 'anova',
                            lower_range_end: int = 20,
                            upper_range_start: int = 80,
                            step_size: int = 2,
                            lower_percentage: int = 2,
                            upper_percentage: int = 98) -> None:
        """
        computes the best upper/lower range per cell based on the anomalous
        and non-anomalous images.

        Parameters
        ----------
        non_anomalous_paths
            a list of paths to all non-anomalous images
        anomalous_paths
            a list of paths to all anomalous images
        method
            either 'anova' or 'minmax'
        grid_size

        lower_percentage

        upper_percentage

        Returns
        -------

        """
        self.images_data = process_images(non_anomalous_paths, anomalous_paths, self.grid_size)
        if method=='anova':
            self.best_ranges = compute_best_ranges_anova(images_data=self.images_data, grid_size=self.grid_size, lower_range_end=lower_range_end, 
                                      upper_range_start=upper_range_start, step_size=step_size)    
        elif method=='minmax':
            self.best_ranges = compute_best_ranges_minmax(images_data=self.images_data, grid_size=self.grid_size)
        else:
            print("Argument for method should be either 'anova' or 'minmax'.")
        

    def compute_anomaly_likelihoods(self, image_paths: []) -> pd.DataFrame:
        """
        computes the likelihood of each cell of each image being anomalous.

        Parameters
        ----------
        image_paths

        Returns
        -------
            a list of arrays, each of size self.grid_size X self.grid_size.
            Each array corresponds to one image, and each cell represents the
            likelihood of that cell of the image being anomalous.
        """
        data = []
        for image_path in tqdm(image_paths, desc="Computing Anomaly Likelihoods"):
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            height, width = image.shape
            cell_height = height // self.grid_size
            cell_width = width // self.grid_size

            image_data = []
            for row in range(self.grid_size):
                for column in range(self.grid_size):
                    y1 = row * cell_height
                    y2 = (row + 1) * cell_height
                    x1 = column * cell_width
                    x2 = (column + 1) * cell_width

                    cell = image[y1:y2, x1:x2]
                    cell_pixel_avg = np.mean(cell)

                    best_upper_range_val = self.best_ranges.loc[
                        (self.best_ranges['row'] == row) & 
                        (self.best_ranges['column'] == column), 
                        'best_upper_range_val'
                    ].values[0]

                    best_lower_range_val = self.best_ranges.loc[
                        (self.best_ranges['row'] == row) & 
                        (self.best_ranges['column'] == column), 
                        'best_lower_range_val'
                    ].values[0]

                    image_name = os.path.basename(image_path)

                    upper_deviation = best_upper_range_val - cell_pixel_avg
                    lower_deviation = best_lower_range_val - cell_pixel_avg
                    S = abs(upper_deviation) + abs(lower_deviation)

                    image_data.append([
                        image_name,
                        image_path,
                        row,
                        column,
                        cell_pixel_avg,
                        S
                    ])
            data.extend(image_data)

        df_anomaly_likelihoods = pd.DataFrame(data, columns=[
            'image_name', 'image_path', 'row', 'column', 'cell_pixel_avg', 'S'
        ])

        centralized_S = df_anomaly_likelihoods['S'] - df_anomaly_likelihoods.groupby(['row', 'column'])['S'].transform('mean')
        standardized_S = centralized_S / df_anomaly_likelihoods.groupby(['row', 'column'])['S'].transform('std')
        standardized_S = standardized_S.fillna(float('-inf'))
        df_anomaly_likelihoods['standardized_S_Sigmoid'] = standardized_S.apply(sigmoid)
                
        return df_anomaly_likelihoods

    def find_corrupt_images(self,
                            image_paths: [],
                            likelihood_threshold: float = 0.5,
                            min_corrupt_cells: int = 0) -> []:
        """
        identifies an image as anomalous if at least `min_corrupt_cells` of
        cells have values greater than `likelihood_threshold`.

        Parameters
        ----------
        image_paths
        likelihood_threshold
        min_corrupt_cells

        Returns
        -------
            a list of zeros and ones, indicating each image being non-anomalous
            or anomalous, respectively.
        """
        df_corrupt_images = pd.DataFrame()

        image_data = self.compute_anomaly_likelihoods(image_paths)
        image_data['label'] = image_data['standardized_S_Sigmoid'].apply(lambda x: 1 if x > likelihood_threshold else 0)
        
        grouped = image_data.groupby(['image_name'])
        
        for _, group in grouped:
            corrupt_count = group['label'].astype(int).sum()
            if corrupt_count > min_corrupt_cells:
                df_corrupt_images = pd.concat([df_corrupt_images, group], ignore_index=True)
        
        return df_corrupt_images
    
    def plot_corrupt_image(self, image_path: str, df_corrupt_images: pd.DataFrame): 

        """Plot the corrupt image, marking corrupt cells with a purple bounding box based on their labels (0 for 
        non-corrupt and 1 for corrupt). Use a blue colormap to indicate the likelihood of being anomalous, as 
        represented by their sigmoid of standardized S statistic value.

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame containing data for cells to be plotted.
        anomalous_folder_path : str
            Path to the folder containing anomalous images.
        non_anomalous_folder_path : str
            Path to the folder containing non-anomalous images.
        image : str or None, optional
            Name of the image file to plot, by default None (randomly selects one image from `df`).
        image_size : int, optional
            Size of the image in pixels, by default 2048.
        grid_size : int, optional
            The size of the grid (rows, columns) used to divide each image, by default 8.
        save : bool, optional
            Whether to save the plot, by default False.
        save_path : str, optional
            Directory path to save the plot if 'save' is True, by default None.
        """
        img = Image.open(image_path)
        width, height = img.size

        fig, ax = plt.subplots()
        ax.imshow(img, cmap='gray')

        cell_width = width // self.grid_size
        cell_height = height // self.grid_size

        scalar_map = ScalarMappable(norm=Normalize(vmin=0, vmax=1), cmap=plt.cm.Blues)

        df_image = df_corrupt_images[df_corrupt_images['image_path'] == image_path]

        for _, row in df_image.iterrows():
            cell_row, cell_col = row['row'], row['column']
            x, y = cell_col * cell_width, cell_row * cell_height
            color = scalar_map.to_rgba(row['standardized_S_Sigmoid'], alpha=0.5)
            edge_color = to_rgba('purple', alpha=1) if row['label'] == 1 else 'none'
            rect = patches.Rectangle((x, y), cell_width, cell_height,
                                    linewidth=2, edgecolor=edge_color,
                                    facecolor=color)
            ax.add_patch(rect)

        ax.set_xticks([])
        ax.set_yticks([])
        scalar_map.set_array([])
        fig.colorbar(scalar_map, ax=ax, orientation='vertical', label='Standardized S Sigmoid')

        plt.show()