# Video-Processing-and-Image-Extraction: Crop and Rotate Frames (Folder - Video Frames Processing)
This project provides tools to extract and process frames from video and images for tasks such as graph data extraction, image rotation, cropping, renaming, and visualization.

## Project Structure
```
Video-Processing-and-Image-Extraction/
│
├── image_processing/
│   ├── rotate_images.py
│   ├── crop_images.py
│   ├── rename_and_zip.py
│   ├── visualize_image_grids.py
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

### 5. `image_processing/visualize_image_grids.py`
- Arranges images into 3x4 grids.
- Adds image index on each image.
- Maintains original scaling.

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
```

📌 Usage Overview
1. Extract Frames
```
from video_processing.video_to_frames import video_to_frames_time_range_and_zip

video_to_frames_time_range_and_zip(
    video_path='input.mp4',
    output_folder='frames/',
    zip_filename='frames.zip',
    start_time_sec=0,
    end_time_sec=10,
    frame_rate=1
)
```
2. Rotate Images from ZIP
```
from image_processing.rotate_zip_images import rotate_images_from_zip

rotate_images_from_zip('frames.zip', 'rotated_frames/', angle=90)
```
3. Visualize as Grid (To figure out pixel range for cropping)
```
from image_processing.visualize_image_grid import create_image_grid

create_image_grid(
    image_folder='rotated_frames',
    output_folder='image_grids',
    cols=3,
    rows=4
)
```
4. Crop Images
```
from image_processing.crop_images import crop_images_in_folder

crop_images_in_folder('rotated_frames/', left=100, top=200, right=600, bottom=500)
```
5. Rename and Zip
```
from image_processing.rename_and_zip import rename_images_and_zip

rename_images_and_zip('rotated_frames/cropped_images', 'processed_images.zip')
```
