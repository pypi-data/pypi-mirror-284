import os

from sklearn.metrics import f1_score, confusion_matrix


def create_labels(anomalous_paths, corrupt_images, test_img_paths):
    """Create true and predicted labels for test images to evaluate their corruption status.

    Parameters
    ----------
    anomalous_paths : List[str]
        Path of anomalous images.
    corrupt_images : pd.DataFrame
        DataFrame containing information on predicted corrupt images.
    test_img_paths : List[str]
        List of test image paths.

    Returns
    -------
    y_true : List[int]
        True labels indicating if the image is anomalous (1) or not (0).
    y_pred : List[int]
        Predicted labels indicating if the image is corrupt (1) or not (0).
    """
    y_true = []
    y_pred = []

    corrupt_imgs_names = corrupt_images['image_name'].unique()
    test_img_names = [os.path.basename(img_path) for img_path in test_img_paths]
    anomalous_image_basenames = [os.path.basename(path) for path in anomalous_paths]

    for test_img_name in test_img_names:
        y_pred.append(1 if test_img_name in corrupt_imgs_names else 0)
        y_true.append(1 if test_img_name in anomalous_image_basenames else 0)
    
    return y_true, y_pred


def f1_metric(anomalous_paths, corrupt_images, test_img_paths):
    """Evaluate the model performance using F1 score and confusion matrix.

    Parameters
    ----------
    anomalous_paths : List[str]
        Paths of anomalous images.
    corrupt_images : pd.DataFrame
        DataFrame containing information on predicted corrupt images.
    test_img_paths : List[str]
        List of test image paths.

    Returns
    -------
    f1_val : float
        The F1 score of the model.
    TP : int
        Number of true positives.
    FP : int
        Number of false positives.
    TN : int
        Number of true negatives.
    FN : int
        Number of false negatives.
    """
    y_true, y_pred = create_labels(anomalous_paths, corrupt_images, test_img_paths)

    F1 = f1_score(y_true, y_pred)

    CM = confusion_matrix(y_true, y_pred)

    TN, FP = CM[0][0], CM[0][1]
    FN, TP = CM[1][0], CM[1][1]

    return F1, TP, FP, TN, FN