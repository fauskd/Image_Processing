from skimage import io, img_as_ubyte
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = img_as_ubyte(io.imread('monalisa.jpg', as_gray = True))

uniform_img = ndimage.uniform_filter(img, size = 9)
plt.imshow(uniform_img)

gaussian_img = ndimage.gaussian_filter(img, sigma = 9)
plt.imshow(gaussian_img)

median_img = ndimage.median_filter(img, 9)
plt.imshow(median_img)