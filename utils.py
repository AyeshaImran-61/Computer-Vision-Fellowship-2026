# ==========================================================
# Vision Toolkit
# utils.py
# ==========================================================

import cv2
import numpy as np


# ==========================================================
# Image Information
# ==========================================================

def image_information(image):
    """
    Returns image metadata.
    """

    height, width = image.shape[:2]

    if len(image.shape) == 2:
        channels = 1
    else:
        channels = image.shape[2]

    resolution = f"{width} × {height}"

    # Approximate memory size
    size_kb = image.nbytes / 1024

    if size_kb < 1024:
        size = f"{size_kb:.2f} KB"
    else:
        size = f"{size_kb / 1024:.2f} MB"

    return {
        "width": width,
        "height": height,
        "channels": channels,
        "resolution": resolution,
        "size": size
    }


# ==========================================================
# Convert Image to Bytes
# ==========================================================

def convert_to_bytes(image):
    """
    Convert a NumPy image into PNG bytes for Streamlit
    download_button().
    """

    if len(image.shape) == 2:

        success, buffer = cv2.imencode(
            ".png",
            image
        )

    else:

        bgr = cv2.cvtColor(
            image,
            cv2.COLOR_RGB2BGR
        )

        success, buffer = cv2.imencode(
            ".png",
            bgr
        )

    if not success:
        raise ValueError("Failed to encode image.")

    return buffer.tobytes()


# ==========================================================
# Reset Image
# ==========================================================

def reset_image(original_image):
    """
    Return a fresh copy of the original image.
    """

    return original_image.copy()


# ==========================================================
# Validate Image
# ==========================================================

def validate_image(image):
    """
    Check whether the image is valid.
    """

    if image is None:
        return False

    if not isinstance(image, np.ndarray):
        return False

    if image.size == 0:
        return False

    return True


# ==========================================================
# RGB to Grayscale Utility
# ==========================================================

def rgb_to_gray(image):
    """
    Convert RGB image to grayscale.
    """

    if len(image.shape) == 2:
        return image

    return cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )


# ==========================================================
# RGB to BGR Utility
# ==========================================================

def rgb_to_bgr(image):
    """
    Convert RGB image to BGR.
    """

    if len(image.shape) == 2:
        return image

    return cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR
    )


# ==========================================================
# BGR to RGB Utility
# ==========================================================

def bgr_to_rgb(image):
    """
    Convert BGR image to RGB.
    """

    if len(image.shape) == 2:
        return image

    return cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )