# Video-Processing-and-Image-Extraction: Crop and Rotate Frames (Folder - Video Frames Processing)
This project provides tools to extract and process frames from video and images for tasks such as graph data extraction, image rotation, cropping, renaming, and visualization.

Video-processing-and-image-extraction/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── video_processing/
│   └── extract_frames.py
│
├── image_processing/
│   ├── rotate_images.py
│   ├── crop_images.py
│   ├── rename_and_zip.py
│   ├── create_image_grids.py
│
├── plotting/
│   └── plot_pixels.py
│
└── utils/
    └── helpers.py  # (optional helper functions, if needed)


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

```bash
pip install -r requirements.txt
