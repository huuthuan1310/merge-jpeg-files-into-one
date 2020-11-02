from PIL import Image

size = 256
x_size = 0
y_size = 0
x_max = 270
y_max = 284

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
        img = Image.open(f'../temp/{x}_{y}_17.jpeg')
        new_img.paste(img, (x_size, y_size))
        print(f'Paste image: {x_size}, {y_size}')

new_img.save('merged.png', "PNG")
print('Merged Completed!!!')
