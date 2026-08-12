# Vision Toolkit — Architecture Documentation

**Student:** Ayesha Imran
**University:** The University of Faisalabad
**Fellowship:** AI Summer Fellowship 2026 — Computer Vision Track

## 1. System Overview

Vision Toolkit is a browser-based computer vision application developed using **Python, Streamlit, OpenCV, NumPy, and Matplotlib**.

The application accepts an image through file upload or browser camera capture, performs the selected computer vision operation, displays the result, and allows the processed image to be downloaded.

## 2. Architecture Diagram

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │     Image Input         │
                │                         │
                │  • File Upload          │
                │  • Webcam Capture       │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │   OpenCV Processing     │
                │                         │
                │ • Grayscale             │
                │ • Blur                  │
                │ • Canny Edge Detection  │
                │ • Thresholding          │
                │ • Transformations       │
                │ • Drawing               │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │     Visualization       │
                │                         │
                │ • Original Image        │
                │ • Processed Image       │
                │ • Histogram             │
                │ • Image Information     │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │         Output          │
                │                         │
                │ • Display Result        │
                │ • Save / Download       │
                └─────────────────────────┘
```

## 3. Architecture Stages

### User

The user interacts with the Streamlit interface and selects the required image processing operation.

### Image Input

The application receives an image either through an uploaded JPG/PNG file or through the browser webcam. Streamlit's `st.camera_input()` returns the captured image as an uploaded-file object that can be processed with Python and OpenCV.

### OpenCV Processing

OpenCV performs the core computer vision operations. Depending on the selected operation, the application can convert the image to grayscale, blur it, detect edges, apply thresholding, adjust brightness or contrast, resize, rotate, crop, or draw shapes and text.

### Visualization

The processed image is displayed in the Streamlit interface. Image information such as width, height, resolution, file size, and color channels is also presented. Histogram visualization provides an additional way to analyze pixel-intensity distribution.

### Output

The final processed image can be saved or downloaded by the user. Streamlit provides `st.download_button()` for downloading generated binary data such as processed images.

## 4. Technologies

| Component            | Technology   |
| -------------------- | ------------ |
| Programming Language | Python       |
| Computer Vision      | OpenCV       |
| Numerical Processing | NumPy        |
| Visualization        | Matplotlib   |
| Web Interface        | Streamlit    |
| Development          | VS Code      |
| Version Control      | Git / GitHub |

## 5. Data Flow

```text
Input Image
    ↓
NumPy Array
    ↓
OpenCV Operation
    ↓
Processed NumPy Array
    ↓
Streamlit Visualization
    ↓
Downloadable Image
```

## 6. Conclusion

The architecture separates the user interface, image input, computer vision processing, visualization, and output stages into a simple and understandable pipeline. This structure provides a foundation for extending the application toward advanced computer vision tasks such as object detection, segmentation, and video analytics.
