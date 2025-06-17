import os
import zipfile
import shutil
from PIL import Image

def rotate_images_from_zip(zip_path, output_folder, angle):
    temp_extract_folder = os.path.join(os.path.dirname(zip_path), "temp_extracted_images")

    if os.path.exists(temp_extract_folder):
        shutil.rmtree(temp_extract_folder)
    os.makedirs(temp_extract_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_extract_folder)

        for filename in os.listdir(temp_extract_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                path = os.path.join(temp_extract_folder, filename)
                output_path = os.path.join(output_folder, filename)
                try:
                    with Image.open(path) as img:
                        rotated_img = img.rotate(angle, expand=True)
                        rotated_img.save(output_path)
                except Exception as e:
                    print(f"Failed to rotate {filename}: {e}")

    finally:
        shutil.rmtree(temp_extract_folder, ignore_errors=True)
