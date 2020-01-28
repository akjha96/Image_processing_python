import sys
from os import path, listdir, makedirs
from PIL import Image

input_location = sys.argv[1]
output_location = sys.argv[2]

# Create a new dir with name and location in specified path
if not path.exists(output_location):
    makedirs(output_location)
# going to input folder and sort all not .png files
for image in listdir(input_location):
    img = Image.open(f'{input_location}{image}')
    clean_name = path.splitext(image)
# now convert the images  and save it in output location
    if '.png' not in clean_name[1]:
        img.save(f'{output_location}{clean_name[0]}.png', 'png')
        print(f"{image} to {clean_name[0]}.png SUCCESS")
    else:
        print(f"{image} is already a png file DISCARDED")

