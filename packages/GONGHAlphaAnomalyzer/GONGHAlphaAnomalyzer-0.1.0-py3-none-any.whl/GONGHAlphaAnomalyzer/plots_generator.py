import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KernelDensity
from tqdm import tqdm

def plot_cell_wise_hist_plot(df, col, grid_size=8, kde_flag=False, save=False, save_path=None):
    """Plot cell-wise histograms for a specified column in a DataFrame for each grid cell.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing the data.
    col : _type_
        Column name for which histograms are to be plotted.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.
    kde_flag : bool, optional
        Whether to plot Kernel Density Estimate (KDE) on top of histograms, by default False.
    save : bool, optional
        Whether to save the plot, by default False.
    save_path : _type_, optional
        Directory path to save the plot if 'save' is True, by default None.
    """
    _, axs = plt.subplots(grid_size, grid_size, figsize=(20, 20))
    axs = axs.flatten()

    for i, (cell_row, cell_col) in enumerate([(r, c) for r in range(grid_size) for c in range(grid_size)]):
        cell_data = df[(df['row'] == cell_row) & (df['column'] == cell_col)]
        axs[i].hist(cell_data[col], bins=20, alpha=0.7, color='skyblue', edgecolor='black', density=True)

        if kde_flag:
            kde = KernelDensity(bandwidth=0.5, kernel='gaussian')
            kde.fit(cell_data[col].values[:, np.newaxis])
            x = np.linspace(cell_data[col].min(), cell_data[col].max(), 1000)
            axs[i].plot(x, np.exp(kde.score_samples(x[:, np.newaxis])), color='r')

        axs[i].set_title(f'Cell ({cell_row}, {cell_col})' if cell_row == 0 else '')
        axs[i].set_xlabel(col if cell_row == grid_size-1 else '')
        axs[i].set_ylabel('Frequency' if cell_col == 0 else '')
        
        if cell_row != grid_size-1:
            axs[i].set_xticklabels([])
        else:
            axs[i].tick_params(axis='x', labelsize=12)

        if cell_col != 0:
            axs[i].set_yticklabels([])
        else:
            axs[i].tick_params(axis='y', labelsize=12)

    plt.subplots_adjust(wspace=0.1, hspace=0.1)

    if save and save_path:
        os.makedirs(save_path, exist_ok=True)
        save_file_path = os.path.join(save_path, f'cell_{col}_hist_plot.pdf')
        plt.savefig(save_file_path)
    elif save:
        print("Warning: save_path is None. Skipping save operation.")

    plt.show()

def plot_cell_wise_scatter(df, col1, col2, grid_size=8, save=False, save_path=None):
    """Plot cell-wise scatter plots for given columns in a DataFrame for each grid cell.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing the data.
    col1 : str
        Name of the first column for the scatter plot.
    col2 : str
        Name of the second column for the scatter plot.
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.
    save : bool, optional
        Whether to save the plot, by default False.
    save_path : _type_, optional
        Directory path to save the plot if 'save' is True, by default None.
    """
    _, axs = plt.subplots(grid_size, grid_size, figsize=(20, 20))
    axs = axs.flatten()

    for i, (cell_row, cell_col) in enumerate([(r, c) for r in range(grid_size) for c in range(grid_size)]):
        cell_data = df[(df['row'] == cell_row) & (df['column'] == cell_col)]
        axs[i].scatter(cell_data[col1], cell_data[col2], alpha=0.7)

        axs[i].set_title(f'Cell ({cell_row}, {cell_col})' if cell_row == 0 else '')
        axs[i].set_xlabel(col1 if cell_row == grid_size-1 else '')
        axs[i].set_ylabel(col2 if cell_col == 0 else '')
        
        axs[i].tick_params(axis='x', labelsize=12)
        if cell_col != 0:
            axs[i].set_yticklabels([])
        else:
            axs[i].tick_params(axis='y', labelsize=12)

    plt.subplots_adjust(wspace=0.1, hspace=0.2)

    if save and save_path:
        os.makedirs(save_path, exist_ok=True)
        save_file_path = os.path.join(save_path, f'cell_{col1}_{col2}_scatter_plot.pdf')
        plt.savefig(save_file_path)
    elif save:
        print("Warning: save_path is None. Skipping save operation.")

    plt.show()


def plot_cell_avg(images_data, best_ranges, grid_size=8, kde_flag=False, save=False, save_path=None):
    """Plot histograms of average pixel values for each grid cell with KDE and normal range indicators.

    Parameters
    ----------
    cell_avg_CSV : str
        Path to the CSV file containing average pixel values for each cell.
    best_ranges_CSV : str
        Path to the CSV file containing the best range values ('best_upper_range_val', 'best_lower_range_val') for
        each grid cell ('row', 'column').
    grid_size : int, optional
        The size of the grid (rows, columns) used to divide each image, by default 8.
    save : bool, optional
        Whether to save the plot, by default False.
    save_path : _type_, optional
        Directory path to save the plot if 'save' is True, by default None.
    """
    _, axs = plt.subplots(grid_size, grid_size, figsize=(16, 16))
    axs = axs.flatten()

    for i, (cell, group) in enumerate(images_data.groupby(['row', 'column'])):
        ax = axs[i]
        upper_range_val = best_ranges.loc[
            (best_ranges['row'] == cell[0]) & (best_ranges['column'] == cell[1]),
            'best_upper_range_val'
        ].values[0]

        lower_range_val = best_ranges.loc[
            (best_ranges['row'] == cell[0]) & (best_ranges['column'] == cell[1]),
            'best_lower_range_val'
        ].values[0]

        images_data_data_curr = images_data[(images_data['row'] == cell[0]) & (images_data['column'] == cell[1])]
        ax.hist(group['cell_pixel_avg'], bins=10, alpha=0.7, color='skyblue', edgecolor='black', density=True)

        if kde_flag:
            kde = KernelDensity(bandwidth=0.5, kernel='gaussian')
            kde.fit(images_data_data_curr['cell_pixel_avg'].values[:, np.newaxis])
            x = np.linspace(images_data_data_curr['cell_pixel_avg'].min(), images_data_data_curr['cell_pixel_avg'].max(), 1000)
            ax.plot(x, np.exp(kde.score_samples(x[:, np.newaxis])), color='r')

        ax.axvline(x=upper_range_val, color='blue', linestyle='--')
        ax.axvline(x=lower_range_val, color='blue', linestyle='--')
        ax.set_title(f'Cell {cell}' if cell[0] == 0 else '')
        ax.set_xlabel('Average Pixel Value' if cell[0] == grid_size-1 else '')
        ax.set_ylabel('Density' if cell[1] == 0 else '')
        ax.set_xlim(0, 255)
        ax.set_ylim(0, 0.1)

        if cell[1] != 0:
            ax.set_yticklabels([])
        else:
            ax.tick_params(axis='y', labelsize=12)

        if cell[0] != grid_size-1:
            axs[i].set_xticklabels([])
        else:
            axs[i].tick_params(axis='x', labelsize=12)

        ax.text(
            0.95, 0.95, 
            f'L - {lower_range_val:.2f}\nU - {upper_range_val:.2f}', 
            verticalalignment='top', 
            horizontalalignment='right', 
            transform=ax.transAxes, 
            color='blue', 
            fontsize=8, 
            bbox=dict(facecolor='white', alpha=0.5)
        )

    plt.subplots_adjust(wspace=0.1, hspace=0.2)

    if save and save_path:
        os.makedirs(save_path, exist_ok=True)
        save_file_path = os.path.join(save_path, 'cell_pixel_avg_plot.pdf')
        plt.savefig(save_file_path)
    elif save:
        print("Warning: save_path is None. Skipping save operation.")

    plt.show()


def get_plot_data(images_data, best_ranges):
    """Prepare plot data to include the following for all cells of the training images: average pixel values, 
    S statistic, centralized S statistic, standardized S statistic, sigmoid of centralized S statistic, and sigmoid of 
    standardized S statistic.

    Parameters
    ----------
    images_data : pd.DataFrame
        DataFrame containing information about sampled images' cells, including 'image_name', 'row', 'column' and 
        'cell_pixel_avg'.
    best_ranges : pd.DataFrame
        DataFrame containing the best range values for each grid cell ('row', 'column'), including
        'best_upper_range_val' and 'best_lower_range_val'.

    Returns
    -------
    pd.DataFrame
        DataFrame with additional columns:
        - 'image_name': Name of the image.
        - 'row': Row index of the grid cell.
        - 'column': Column index of the grid cell.
        - 'cell_pixel_avg': Average pixel value of the cell.
        - 'S': Metric calculated based on difference of average pixel value from best range values.
        - 'centralized_S': S after centralizing by subtracting mean S for each (row, column) group.
        - 'standardized_S': S after standardizing by dividing centralized S by standard deviation S (fills nan values 
        with -inf for their Sigmoid to be 0).
        - 'centralized_S_Sigmoid': Sigmoid transformation of centralized_S.
        - 'standardized_S_Sigmoid': Sigmoid transformation of standardized_S.
    """
    all_data = []
    images_data = images_data.drop_duplicates(subset=['image_name', 'row', 'column'])

    for _, row in tqdm(images_data.iterrows(), total=images_data.shape[0], desc="Preparing Plotting Data"):
        best_upper_range_val = best_ranges.loc[
            (best_ranges['row'] == row['row']) & 
            (best_ranges['column'] == row['column']), 
            'best_upper_range_val'
        ].values[0]

        best_lower_range_val = best_ranges.loc[
            (best_ranges['row'] == row['row']) & 
            (best_ranges['column'] == row['column']), 
            'best_lower_range_val'
        ].values[0]

        S = abs(best_upper_range_val - row['cell_pixel_avg']) + abs(best_lower_range_val - row['cell_pixel_avg'])

        all_data.append({
            'image_name': row['image_name'],
            'row': row['row'],
            'column': row['column'],
            'cell_pixel_avg': row['cell_pixel_avg'],
            'S': S
        })

    df = pd.DataFrame(all_data, columns=['image_name', 'row', 'column', 'cell_pixel_avg', 'S'])
    df['centralized_S'] = df['S'] - df.groupby(['row', 'column'])['S'].transform('mean')
    df['standardized_S'] = (df['centralized_S']) / df.groupby(['row', 'column'])['S'].transform('std')
    df['standardized_S'] = df['standardized_S'].fillna(float('-inf'))
    df['standardized_S_Sigmoid'] = df['standardized_S'].apply(sigmoid)
    
    return df


def sigmoid(x):
    """Compute the sigmoid of a float number.

    Parameters
    ----------
    x : float
        Input value.

    Returns
    -------
    float
        Sigmoid of `x`, calculated as `1 / (1 + exp(-x))`. The output is normalized to the range between 0 and 1.
    """
    return 1 / (1 + np.exp(-x))