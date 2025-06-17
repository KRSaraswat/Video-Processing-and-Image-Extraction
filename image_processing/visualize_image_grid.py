import os
from PIL import Image, ImageDraw, ImageFont
import math

def create_image_grid(image_folder, output_folder, cols=3, rows=4):
    image_files = sorted([
        f for f in os.listdir(image_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
    ])
    total = len(image_files)
    images_per_grid = cols * rows
    grids = math.ceil(total / images_per_grid)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    try:
        font = ImageFont.truetype(font_path, 30)
    except:
        font = ImageFont.load_default()

    idx = 0
    for grid_idx in range(grids):
        grid_images = image_files[idx:idx+images_per_grid]

        cell_width = max(Image.open(os.path.join(image_folder, img)).width for img in grid_images)
        cell_height = max(Image.open(os.path.join(image_folder, img)).height for img in grid_images)

        canvas = Image.new('RGB', (cols * cell_width, rows * cell_height), 'white')
        draw = ImageDraw.Draw(canvas)

        for i, img_file in enumerate(grid_images):
            r, c = divmod(i, cols)
            x = c * cell_width
            y = r * cell_height
            number = idx + i + 1
            with Image.open(os.path.join(image_folder, img_file)) as img:
                canvas.paste(img, (x, y))
                draw.text((x+10, y+10), str(number), font=font, fill='white')

        output_path = os.path.join(output_folder, f"image_grid_{grid_idx+1:03d}.png")
        canvas.save(output_path)
        idx += images_per_grid
