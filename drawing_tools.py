# ==========================================================
# Vision Toolkit
# drawing_tools.py
# ==========================================================

import cv2


# ==========================================================
# Draw Rectangle
# ==========================================================

def draw_rectangle(
    image,
    x,
    y,
    width,
    height,
    color=(255, 0, 0),
    thickness=2
):
    """
    Draw a rectangle on the image.
    """

    output = image.copy()

    cv2.rectangle(
        output,
        (x, y),
        (x + width, y + height),
        color,
        thickness
    )

    return output


# ==========================================================
# Draw Circle
# ==========================================================

def draw_circle(
    image,
    center_x,
    center_y,
    radius,
    color=(0, 255, 0),
    thickness=2
):
    """
    Draw a circle on the image.
    """

    output = image.copy()

    cv2.circle(
        output,
        (center_x, center_y),
        radius,
        color,
        thickness
    )

    return output


# ==========================================================
# Draw Line
# ==========================================================

def draw_line(
    image,
    x1,
    y1,
    x2,
    y2,
    color=(0, 0, 255),
    thickness=2
):
    """
    Draw a line on the image.
    """

    output = image.copy()

    cv2.line(
        output,
        (x1, y1),
        (x2, y2),
        color,
        thickness
    )

    return output


# ==========================================================
# Add Text
# ==========================================================

def add_text(
    image,
    text,
    x,
    y,
    font_scale=1.0,
    color=(255, 255, 0),
    thickness=2
):
    """
    Add text to the image.
    """

    output = image.copy()

    cv2.putText(
        output,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )

    return output