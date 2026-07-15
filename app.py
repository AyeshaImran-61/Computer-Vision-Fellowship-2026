# ==========================================================
# Vision Toolkit
# app.py
# Streamlit Main Application
# ==========================================================

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from image_processing import (
    grayscale,
    canny_edge,
    gaussian_blur,
    median_blur,
    binary_threshold,
    adaptive_threshold,
    otsu_threshold,
    adjust_brightness,
    adjust_contrast,
    rotate_image,
    resize_image,
    crop_image,
    calculate_histogram,
    save_image
)

from drawing_tools import (
    draw_rectangle,
    draw_circle,
    draw_line,
    add_text
)

from webcam import capture_from_webcam

from utils import (
    image_information,
    convert_to_bytes
)

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title="Vision Toolkit",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Vision Toolkit")
st.markdown(
    "A Professional Computer Vision Toolkit built with **OpenCV + Streamlit**"
)

# ==========================================================
# Session State
# ==========================================================

if "original_image" not in st.session_state:
    st.session_state.original_image = None

if "processed_image" not in st.session_state:
    st.session_state.processed_image = None

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("Controls")

image_source = st.sidebar.radio(
    "Choose Image Source",
    [
        "Upload Image",
        "Webcam"
    ]
)

# ==========================================================
# Upload Image
# ==========================================================

if image_source == "Upload Image":

    uploaded_file = st.sidebar.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")

        image = np.array(image)

        st.session_state.original_image = image.copy()
        st.session_state.processed_image = image.copy()

# ==========================================================
# Webcam
# ==========================================================

if image_source == "Webcam":

    if st.sidebar.button("Capture Image"):

        frame = capture_from_webcam()

        if frame is not None:

            st.session_state.original_image = frame.copy()
            st.session_state.processed_image = frame.copy()

# ==========================================================
# Stop if no image
# ==========================================================

if st.session_state.processed_image is None:

    st.info("Upload an image or capture one using the webcam.")

    st.stop()

image = st.session_state.processed_image

# ==========================================================
# Image Information
# ==========================================================

st.sidebar.header("Image Information")

info = image_information(image)

st.sidebar.write(f"Width : {info['width']} px")
st.sidebar.write(f"Height : {info['height']} px")
st.sidebar.write(f"Channels : {info['channels']}")
st.sidebar.write(f"Resolution : {info['resolution']}")
st.sidebar.write(f"File Size : {info['size']}")

# ==========================================================
# Processing Menu
# ==========================================================

operation = st.sidebar.selectbox(
    "Select Operation",
    [

        "Original",

        "Grayscale",

        "Canny Edge Detection",

        "Gaussian Blur",

        "Median Blur",

        "Binary Threshold",

        "Adaptive Threshold",

        "Otsu Threshold",

        "Brightness",

        "Contrast",

        "Rotate",

        "Resize",

        "Crop",

        "Draw Rectangle",

        "Draw Circle",

        "Draw Line",

        "Add Text",

        "Histogram"

    ]
)

processed = image.copy()

# ==========================================================
# Original
# ==========================================================

if operation == "Original":

    processed = image.copy()

# ==========================================================
# Grayscale
# ==========================================================

elif operation == "Grayscale":

    processed = grayscale(image)

# ==========================================================
# Canny Edge
# ==========================================================

elif operation == "Canny Edge Detection":

    t1 = st.sidebar.slider(
        "Threshold 1",
        0,
        255,
        100
    )

    t2 = st.sidebar.slider(
        "Threshold 2",
        0,
        255,
        200
    )

    processed = canny_edge(
        image,
        t1,
        t2
    )

# ==========================================================
# Gaussian Blur
# ==========================================================

elif operation == "Gaussian Blur":

    k = st.sidebar.slider(
        "Kernel Size",
        1,
        31,
        5,
        step=2
    )

    processed = gaussian_blur(
        image,
        k
    )

# ==========================================================
# Median Blur
# ==========================================================

elif operation == "Median Blur":

    k = st.sidebar.slider(
        "Kernel Size",
        1,
        31,
        5,
        step=2
    )

    processed = median_blur(
        image,
        k
    )# ==========================================================
# Binary Threshold
# ==========================================================

elif operation == "Binary Threshold":

    threshold_value = st.sidebar.slider(
        "Threshold Value",
        0,
        255,
        127
    )

    processed = binary_threshold(
        image,
        threshold_value
    )

# ==========================================================
# Adaptive Threshold
# ==========================================================

elif operation == "Adaptive Threshold":

    block_size = st.sidebar.slider(
        "Block Size",
        3,
        51,
        11,
        step=2
    )

    constant = st.sidebar.slider(
        "Constant (C)",
        0,
        20,
        2
    )

    processed = adaptive_threshold(
        image,
        block_size,
        constant
    )

# ==========================================================
# Otsu Threshold
# ==========================================================

elif operation == "Otsu Threshold":

    processed = otsu_threshold(image)

# ==========================================================
# Brightness
# ==========================================================

elif operation == "Brightness":

    brightness = st.sidebar.slider(
        "Brightness",
        -100,
        100,
        0
    )

    processed = adjust_brightness(
        image,
        brightness
    )

# ==========================================================
# Contrast
# ==========================================================

elif operation == "Contrast":

    contrast = st.sidebar.slider(
        "Contrast",
        0.5,
        3.0,
        1.0,
        0.1
    )

    processed = adjust_contrast(
        image,
        contrast
    )

# ==========================================================
# Rotate
# ==========================================================

elif operation == "Rotate":

    angle = st.sidebar.slider(
        "Rotation Angle",
        -180,
        180,
        0
    )

    processed = rotate_image(
        image,
        angle
    )

# ==========================================================
# Resize
# ==========================================================

elif operation == "Resize":

    width = st.sidebar.number_input(
        "Width",
        50,
        3000,
        image.shape[1]
    )

    height = st.sidebar.number_input(
        "Height",
        50,
        3000,
        image.shape[0]
    )

    processed = resize_image(
        image,
        int(width),
        int(height)
    )

# ==========================================================
# Crop
# ==========================================================

elif operation == "Crop":

    h, w = image.shape[:2]

    x1 = st.sidebar.slider(
        "Start X",
        0,
        w - 1,
        0
    )

    y1 = st.sidebar.slider(
        "Start Y",
        0,
        h - 1,
        0
    )

    x2 = st.sidebar.slider(
        "End X",
        x1 + 1,
        w,
        w
    )

    y2 = st.sidebar.slider(
        "End Y",
        y1 + 1,
        h,
        h
    )

    processed = crop_image(
        image,
        x1,
        y1,
        x2,
        y2
    )

# ==========================================================
# Draw Rectangle
# ==========================================================

elif operation == "Draw Rectangle":

    x = st.sidebar.number_input(
        "X",
        0,
        image.shape[1],
        50
    )

    y = st.sidebar.number_input(
        "Y",
        0,
        image.shape[0],
        50
    )

    width = st.sidebar.number_input(
        "Width",
        10,
        image.shape[1],
        200
    )

    height = st.sidebar.number_input(
        "Height",
        10,
        image.shape[0],
        150
    )

    processed = draw_rectangle(
        image,
        int(x),
        int(y),
        int(width),
        int(height)
    )

# ==========================================================
# Draw Circle
# ==========================================================

elif operation == "Draw Circle":

    center_x = st.sidebar.number_input(
        "Center X",
        0,
        image.shape[1],
        image.shape[1] // 2
    )

    center_y = st.sidebar.number_input(
        "Center Y",
        0,
        image.shape[0],
        image.shape[0] // 2
    )

    radius = st.sidebar.slider(
        "Radius",
        5,
        300,
        80
    )

    processed = draw_circle(
        image,
        int(center_x),
        int(center_y),
        int(radius)
    )

# ==========================================================
# Draw Line
# ==========================================================

elif operation == "Draw Line":

    x1 = st.sidebar.number_input(
        "Start X",
        0,
        image.shape[1],
        0
    )

    y1 = st.sidebar.number_input(
        "Start Y",
        0,
        image.shape[0],
        0
    )

    x2 = st.sidebar.number_input(
        "End X",
        0,
        image.shape[1],
        image.shape[1]
    )

    y2 = st.sidebar.number_input(
        "End Y",
        0,
        image.shape[0],
        image.shape[0]
    )

    processed = draw_line(
        image,
        int(x1),
        int(y1),
        int(x2),
        int(y2)
    )# ==========================================================
# Add Text
# ==========================================================

elif operation == "Add Text":

    text = st.sidebar.text_input(
        "Enter Text",
        "Vision Toolkit"
    )

    x = st.sidebar.number_input(
        "Text X",
        0,
        image.shape[1],
        50
    )

    y = st.sidebar.number_input(
        "Text Y",
        0,
        image.shape[0],
        50
    )

    font_scale = st.sidebar.slider(
        "Font Scale",
        0.5,
        5.0,
        1.0,
        0.1
    )

    processed = add_text(
        image,
        text,
        int(x),
        int(y),
        font_scale
    )

# ==========================================================
# Histogram
# ==========================================================

elif operation == "Histogram":

    fig = calculate_histogram(image)

    processed = image.copy()

# ==========================================================
# Store Processed Image
# ==========================================================

st.session_state.processed_image = processed

# ==========================================================
# Before / After Comparison
# ==========================================================

st.markdown("---")
st.subheader("Before / After Comparison")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Original Image")

    st.image(
        st.session_state.original_image,
        channels="RGB",
        use_container_width=True
    )

with col2:

    st.markdown("### Processed Image")

    if len(processed.shape) == 2:

        st.image(
            processed,
            clamp=True,
            use_container_width=True
        )

    else:

        st.image(
            processed,
            channels="RGB",
            use_container_width=True
        )

# ==========================================================
# Histogram Display
# ==========================================================

if operation == "Histogram":

    st.markdown("---")
    st.subheader("Histogram")

    st.pyplot(fig)

# ==========================================================
# Save Image
# ==========================================================

st.markdown("---")

col_save, col_reset = st.columns(2)

with col_save:

    if st.button("💾 Save Processed Image"):

        filename = save_image(processed)

        st.success(f"Image saved successfully as {filename}")

with col_reset:

    if st.button("🔄 Reset Image"):

        st.session_state.processed_image = (
            st.session_state.original_image.copy()
        )

        st.rerun()

# ==========================================================
# Download Button
# ==========================================================

image_bytes = convert_to_bytes(processed)

st.download_button(

    label="⬇ Download Image",

    data=image_bytes,

    file_name="processed_image.png",

    mime="image/png"

)

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">
        Vision Toolkit
        <br>
        Developed using Streamlit + OpenCV
    </div>
    """,
    unsafe_allow_html=True
)