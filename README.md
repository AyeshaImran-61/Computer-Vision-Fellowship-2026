# 🖼️ Vision Toolkit

A professional **Computer Vision Toolkit** built with **Python, OpenCV, and Streamlit**. This application provides an interactive interface for performing common image processing operations, drawing shapes, visualizing histograms, and capturing images from a webcam.

---

# Features

## Image Input
- Upload JPG, JPEG, and PNG images
- Capture images directly from a webcam

## Image Information
- Width
- Height
- Resolution
- Number of Color Channels
- Estimated File Size

## Image Processing
- Grayscale Conversion
- Canny Edge Detection
- Gaussian Blur
- Median Blur
- Binary Threshold
- Adaptive Threshold
- Otsu Threshold
- Brightness Adjustment
- Contrast Adjustment
- Image Rotation
- Image Resize
- Image Cropping

## Drawing Tools
- Draw Rectangle
- Draw Circle
- Draw Line
- Add Custom Text

## Visualization
- RGB Histogram

## Other Features
- Before / After Comparison
- Save Processed Image
- Download Processed Image
- Reset Image
- Professional Streamlit User Interface

---

# Project Structure

```
VisionToolkit/
│
├── app.py
├── image_processing.py
├── drawing_tools.py
├── webcam.py
├── utils.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python 3.11+
- Streamlit
- OpenCV
- NumPy
- Matplotlib
- Pillow

---

# Installation

Clone the repository:

```bash
git clone <repository_url>
```

Move into the project directory:

```bash
cd VisionToolkit
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will automatically open in your web browser.

---

# How to Use

1. Launch the application.
2. Upload an image or capture one from the webcam.
3. Choose an operation from the sidebar.
4. Adjust the available parameters using the sliders or input fields.
5. View the original and processed images side by side.
6. Save or download the processed image.

---

# Screenshots

You can add screenshots of the application here after running it.

Example:

```
screenshots/
│
├── home.png
├── histogram.png
├── drawing_tools.png
└── webcam.png
```

---

# Future Improvements

Possible enhancements include:

- Image Filters
- Morphological Operations
- Face Detection
- Object Detection using YOLO
- Background Removal
- Image Segmentation
- OCR Integration
- Real-Time Webcam Filters
- Batch Image Processing
- Dark Mode UI

---

# Learning Outcomes

This project demonstrates:

- Computer Vision Fundamentals
- OpenCV Image Processing
- Streamlit Web Applications
- Histogram Analysis
- Thresholding Techniques
- Image Transformations
- Drawing Functions
- Webcam Integration
- Python Modular Programming

---

# License

This project is provided for educational and learning purposes.

You are free to modify and extend it for personal, academic, or portfolio use.

---

# Author

Developed using:

- Python
- OpenCV
- Streamlit

Vision Toolkit © 2026