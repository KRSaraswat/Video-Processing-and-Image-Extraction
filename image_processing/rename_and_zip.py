import os
import zipfile

def rename_images_and_zip(folder_path, zip_filename):
    image_files = sorted([
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    for i, old_name in enumerate(image_files):
        ext = os.path.splitext(old_name)[1]
        new_name = f"{i+1}{ext}"
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in os.listdir(folder_path):
            path = os.path.join(folder_path, file)
            zipf.write(path, file)
