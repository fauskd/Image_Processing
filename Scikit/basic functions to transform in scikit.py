from skimage import io
import matplotlib.pyplot as plt

img = io.imread('monalisa.jpg')
plt.imshow(img)


img = io.imread('monalisa.jpg', as_gray = False)
plt.imshow(img)


img = io.imread('monalisa.jpg', as_gray = True)
plt.imshow(img)

from skimage.transform import resize, rescale, downscale_local_mean

rescaled_img = rescale(img, 1.0/4.0, anti_aliasing = False)
plt.imshow(rescaled_img)


resized_img = resize(img, (200,200))
plt.imshow(resized_img)


downscaled_img = downscale_local_mean(img, (4,3))
plt.imshow(downscaled_img)