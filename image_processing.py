# ==========================================================
# Vision Toolkit
# image_processing.py
# ==========================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# ==========================================================
# Grayscale
# ==========================================================

def grayscale(image):
    """
    Convert RGB image to grayscale.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    return gray


# ==========================================================
# Canny Edge Detection
# ==========================================================

def canny_edge(
    image,
    threshold1,
    threshold2
):
    """
    Apply Canny Edge Detection.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    edges = cv2.Canny(
        gray,
        threshold1,
        threshold2
    )

    return edges


# ==========================================================
# Gaussian Blur
# ==========================================================

def gaussian_blur(
    image,
    kernel_size
):
    """
    Apply Gaussian Blur.
    """

    blurred = cv2.GaussianBlur(
        image,
        (kernel_size, kernel_size),
        0
    )

    return blurred


# ==========================================================
# Median Blur
# ==========================================================

def median_blur(
    image,
    kernel_size
):
    """
    Apply Median Blur.
    """

    blurred = cv2.medianBlur(
        image,
        kernel_size
    )

    return blurred


# ==========================================================
# Binary Threshold
# ==========================================================

def binary_threshold(
    image,
    threshold_value
):
    """
    Apply Binary Threshold.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    _, thresh = cv2.threshold(
        gray,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    return thresh


# ==========================================================
# Adaptive Threshold
# ==========================================================

def adaptive_threshold(
    image,
    block_size,
    constant
):
    """
    Apply Adaptive Threshold.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        block_size,
        constant
    )

    return thresh


# ==========================================================
# Otsu Threshold
# ==========================================================

def otsu_threshold(image):
    """
    Apply Otsu Threshold.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresh# ==========================================================
# Brightness Adjustment
# ==========================================================

def adjust_brightness(
    image,
    value
):
    """
    Increase or decrease image brightness.
    """

    image = image.astype(np.int16)

    image = image + value

    image = np.clip(
        image,
        0,
        255
    )

    return image.astype(np.uint8)


# ==========================================================
# Contrast Adjustment
# ==========================================================

def adjust_contrast(
    image,
    alpha
):
    """
    Adjust image contrast.
    alpha > 1 increases contrast.
    alpha < 1 decreases contrast.
    """

    output = cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=0
    )

    return output


# ==========================================================
# Rotate Image
# ==========================================================

def rotate_image(
    image,
    angle
):
    """
    Rotate image around its center.
    """

    height, width = image.shape[:2]

    center = (
        width // 2,
        height // 2
    )

    matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    rotated = cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )

    return rotated


# ==========================================================
# Resize Image
# ==========================================================

def resize_image(
    image,
    width,
    height
):
    """
    Resize image.
    """

    resized = cv2.resize(
        image,
        (width, height),
        interpolation=cv2.INTER_AREA
    )

    return resized


# ==========================================================
# Crop Image
# ==========================================================

def crop_image(
    image,
    x1,
    y1,
    x2,
    y2
):
    """
    Crop image.
    """

    cropped = image[
        y1:y2,
        x1:x2
    ]

    return cropped


# ==========================================================
# Histogram
# ==========================================================

def calculate_histogram(image):
    """
    Generate RGB histogram using Matplotlib.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    colors = (
        "red",
        "green",
        "blue"
    )

    for i, color in enumerate(colors):

        hist = cv2.calcHist(
            [image],
            [i],
            None,
            [256],
            [0, 256]
        )

        ax.plot(
            hist,
            color=color,
            linewidth=2
        )

    ax.set_title("RGB Histogram")
    ax.set_xlabel("Pixel Intensity")
    ax.set_ylabel("Frequency")
    ax.set_xlim([0, 256])
    ax.grid(True)

    return fig


# ==========================================================
# Save Image
# ==========================================================

def save_image(image):
    """
    Save processed image with timestamp.
    """

    filename = (
        "processed_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".png"
    )

    save_image = image

    if len(save_image.shape) == 2:

        cv2.imwrite(
            filename,
            save_image
        )

    else:

        bgr = cv2.cvtColor(
            save_image,
            cv2.COLOR_RGB2BGR
        )

        cv2.imwrite(
            filename,
            bgr
        )

    return filename