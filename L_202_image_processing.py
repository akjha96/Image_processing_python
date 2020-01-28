from PIL import Image, ImageFilter

im = Image.open('profil.jpg')
print(im.format, im.size, im.mode)

source = im.split()
print(source)

# im = Image.merge("RGB", (b, g, r))

out = im.resize((600, 742))
# out = im.rotate(45)


out.show()

# def roll(image, delta):
#     """Roll an image sideways."""
#     xsize, ysize = image.size

#     delta = delta % xsize
#     if delta == 0: return image

#     part1 = image.crop((0, 0, delta, ysize))
#     part2 = image.crop((delta, 0, xsize, ysize))
#     image.paste(part1, (xsize - delta, 0, xsize, ysize))
#     image.paste(part2, (0, 0, xsize - delta, ysize))


# image_roll = roll(im, 455)
# image_roll.show()
