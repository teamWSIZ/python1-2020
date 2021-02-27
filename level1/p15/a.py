from PIL import Image

im = Image.open('1.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((40, 60))
im.save('gg.jpg', 'PNG')

print(im)