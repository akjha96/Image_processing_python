from PIL import Image, ImageFilter
import time

img = Image.open('./Pokedex/pikachu.jpg')
# print(img)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./Pokedex/Blured_pikachu.png', 'png')
filtered_img1 = img.filter(ImageFilter.SMOOTH)
filtered_img1.save('./Pokedex/smoothed_pikachu.png', 'png')
filtered_img2 = img.filter(ImageFilter.SHARPEN)
filtered_img2.save('./Pokedex/sharpened_pikachu.png', 'png')
grey_img = img.convert('L')
grey_img.save('./Pokedex/grey_pikachu.png', 'png')

# resize and rotate
resized = filtered_img1.resize((300, 300))
resized.save('./Pokedex/thumbnail_pikachu.png', 'png')
rotated = resized.rotate(32)
rotated.save('./Pokedex/rotated_pikachu.png', 'png')

# Box and Crop
box = (120, 120, 400, 400)
cropped_img = filtered_img1.crop(box)
cropped_img1 = img.crop(box)
cropped_img.save('./Pokedex/cropped_smoothed_pikachu.png', 'png')
cropped_img1.save('./Pokedex/cropped_pikachu.png', 'png')

# .thumbnail
code_img = Image.open('./code.jpg')
print(code_img.size)
code_img.thumbnail((400, 200))
code_img.save('./code_thumbnail.png', 'png')
print(code_img.size)
