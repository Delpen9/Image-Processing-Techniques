import cv2
import numpy as np

def get_gradient_magnitude_sobel(
    image : np.ndarray
) -> np.ndarray:
    '''
    Computes the gradient magnitude of an image using the Sobel operator.

    Parameters:
        image (ndarray): the image to compute the gradient magnitude of

    Returns:
        ndarray: the gradient magnitude of the image
    '''
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    gradient_magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))

    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude

def threshold_gradient_sobel(
    image : np.ndarray,
    threshold : np.ndarray
) -> np.ndarray:
    '''
    Applies a threshold to the gradient magnitude of an image.

    Parameters:
        image (ndarray): the gradient magnitude image
        threshold (int): the threshold value (0-255)

    Returns:
        ndarray: the thresholded gradient magnitude image
    '''
    assert threshold >= 0
    assert threshold <= 255

    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return thresholded_image

def sobel_edge_detection(
    image: np.ndarray,
    threshold : int = 150
) -> np.ndarray:
    '''
    Creates a gradient magnitude and then applies a threshold to the gradient magnitude of an image.

    Parameters:
        image (ndarray): the gradient magnitude image
        threshold (int): the threshold value (0-255)

    Returns:
        ndarray: the thresholded gradient magnitude image
    '''
    assert threshold >= 0
    assert threshold <= 255

    new_image = image.copy()

    gradient_image = get_gradient_magnitude_sobel(new_image)
    thresholded_gradient = threshold_gradient_sobel(gradient_image, threshold)
    return thresholded_gradient
    