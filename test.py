import os
from PIL import Image

mask_dir = '../data-test/mask'
image_dir = '../data-test/target'
processed_dir = '../data-test/input'

masks = next(os.walk(mask_dir), (None, None, []))[2]
images = next(os.walk(image_dir), (None, None, []))[2]

for idx in range(len(masks)):
    mask_path = os.path.join(mask_dir, masks[idx])
    image_path = os.path.join(image_dir, images[idx])
    processed_image_path = os.path.join(processed_dir, images[idx])
    
    im1 = Image.open(image_path)
    im2 = Image.open(mask_path).resize(im1.size)
    mask = Image.open(mask_path).convert('L').resize(im1.size)
    im = Image.composite(im1, im2, mask)
    im.save(processed_image_path)
    print(f'\r🚀 Masking images: {idx+1}/{len(masks)}. ', end='')
print('Done!')