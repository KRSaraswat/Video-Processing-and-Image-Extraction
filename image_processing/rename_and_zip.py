import os
import zipfile
from PIL import Image

def rename_images_and_zip(folder_path, zip_filename, prefix='', dry_run=False):
    """
    Renames image files in a folder sequentially (optionally with a prefix),
    then zips the renamed images.

    Args:
        folder_path (str): Path to the folder containing images.
        zip_filename (str): Name for the output zip archive.
        prefix (str): Optional prefix to add before numbers.
        dry_run (bool): If True, only simulates renaming without changes.
    """
    if not os.path.isdir(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    image_files = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)],
        key=lambda x: x.lower()
    )

    if not image_files:
        print("⚠️ No image files found. Zipping skipped.")
        return

    print(f"🖼 Found {len(image_files)} image(s) in: {folder_path}")
    renamed_count = 0

    # Renaming step
    for i, old_name in enumerate(image_files):
        ext = os.path.splitext(old_name)[1]
        new_name = f"{prefix}{i + 1}{ext}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        if old_path == new_path:
            print(f"➡️ Skipping (already named): {old_name}")
            continue

        if os.path.exists(new_path):
            print(f"⚠️ Skipping rename, target exists: {new_name}")
            continue

        if dry_run:
            print(f"[DRY-RUN] Would rename '{old_name}' → '{new_name}'")
        else:
            try:
                os.rename(old_path, new_path)
                print(f"✅ Renamed '{old_name}' → '{new_name}'")
                renamed_count += 1
            except OSError as e:
                print(f"❌ Error renaming '{old_name}': {e}")

    if dry_run:
        print("ℹ️ Dry run complete. No changes made.")
        return

    print(f"✔️ Renaming done. Total renamed: {renamed_count}")

    # Zipping step
    print(f"📦 Creating ZIP archive: {zip_filename}")
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in os.listdir(folder_path):
                if file.lower().endswith(image_extensions):
                    filepath = os.path.join(folder_path, file)
                    zipf.write(filepath, os.path.basename(filepath))
        print(f"✅ Zip archive created: {zip_filename}")
    except Exception as e:
        print(f"❌ Error creating zip: {e}")

# Example usage
if __name__ == "__main__":
    target_folder = "/content/rotated_frames/cropped_images"
    output_zip = "/content/renamed_images.zip"
    name_prefix = "img_"  # Optional prefix for filenames
    simulate_only = False  # Set True for preview only

    rename_images_and_zip(
        folder_path=target_folder,
        zip_filename=output_zip,
        prefix=name_prefix,
        dry_run=simulate_only
    )
