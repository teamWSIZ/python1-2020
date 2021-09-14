from PIL import Image
from numpy import asarray
import numpy as np

image = Image.open('kali1.png')
# image.show()
data = asarray(image)
print(data.shape)  # (128, 128, 4)

img1 = Image.fromarray(data, 'RGBA')  # with alpha
img1.show()

img2 = Image.fromarray(data[:, :, 0:3])  # black background
img2.show()
