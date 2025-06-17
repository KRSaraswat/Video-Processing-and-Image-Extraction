# Video-Processing-and-Image-Extraction: Crop and Rotate Frames (Folder - Video Frames Processing)
This project provides tools to extract and process frames from video and images for tasks such as graph data extraction, image rotation, cropping, renaming, and visualization.

## Project Structure
```Video-Processing-and-Image-Extraction/
│
├── image_processing/
│   ├── rotate_images.py
│   ├── crop_images.py
│   ├── rename_and_zip.py
│   ├── create_image_grids.py
│
├── video_processing/
│   └── extract_frames.py
│
├── LICENSE
│
├── README.md
│
└── setup.py
```

## 📦 Modules

### 1. `video_processing/extract_frames.py`
- Extracts frames from a video in a given time range.
- Zips the extracted frames.

### 2. `image_processing/rotate_images.py`
- Rotates all images in a ZIP by a specified angle.

### 3. `image_processing/crop_images.py`
- Crops images in a folder using specified pixel bounds.

### 4. `image_processing/rename_and_zip.py`
- Renames images sequentially and zips the folder.

### 5. `image_processing/create_image_grids.py`
- Arranges images into 3x4 grids.
- Adds image index on each image.
- Maintains original scaling.

### 6. `plotting/plot_pixels.py`
- Displays an image with pixel axes.

## 🛠 Requirements
---

## 🚀 Features

- **Frame Extraction**: Extract frames from video in a specific time range.
- **Rotation**: Rotate all images in a ZIP archive.
- **Grid Visualization**: Arrange images into a grid layout with numbering (Helps in identifying pixel range for cropping).
- **Cropping**: Crop all images in a folder.
- **Renaming and Zipping**: Rename images sequentially and zip them.

---

## ✅ Requirements

- `moviepy`
- `Pillow`
- `numpy`

Install them via:

```bash
pip install moviepy pillow numpy

