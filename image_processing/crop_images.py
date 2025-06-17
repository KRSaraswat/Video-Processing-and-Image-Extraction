import os
from PIL import Image

def crop_images_in_folder(folder_path, left, top, right, bottom):
    output_folder = os.path.join(folder_path, "cropped_images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(path) as img:
                    img_width, img_height = img.size
                    if right <= img_width and bottom <= img_height:
                        cropped_img = img.crop((left, top, right, bottom))
                        cropped_img.save(output_path)
            except Exception as e:
                print(f"Failed to crop {filename}: {e}")
