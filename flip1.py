from skimage import io, img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

img = img_as_ubyte(io.imread('monalisa.jpg', as_gray = True))

flippedLR = np.fliplr(img)
flippedUD = np.flipud(img)

plt.subplot(2, 1,1)
plt.imshow(img, cmap = "Reds")
plt.subplot(2,2,3)
plt.imshow(flippedLR, cmap = 'Blues')
plt.subplot(2,2,4)
plt.imshow(flippedUD, cmap = 'hsv')