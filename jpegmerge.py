from PIL import Image
import os

def jpeg_merge(x_max, y_max, final_name, path, dest_path):
    size = 256
    x_size = 0
    y_size = 0

    for x in range(1, x_max):
        x_size = x_size + size
    for y in range(1, y_max):
        y_size = y_size + size

    print(f'Image size: {x_size}, {y_size}')

    new_img = Image.new('RGB', (x_size, y_size), (250, 250, 250))

    print('Created new image!')

    x_size = -size

    print('Merging images...')

    for x in range(0, x_max):
        x_size = x_size + size
        y_size = -size
        for y in range(0, y_max):
            y_size = y_size + size
            img = Image.open(f'{path}/{x}_{y}.jpeg')
            new_img.paste(img, (x_size, y_size))
    
    output_dir = dest_path
    isDir = os.path.isdir(output_dir)
    if isDir == False:
        os.makedirs(output_dir)
    
    new_img.save(f'{output_dir}/{final_name}.png', "PNG")
    print('Merged Completed!!!')
