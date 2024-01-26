from skimage import io
import matplotlib.pyplot as plt

img = io.imread('monalisa.jpg', as_gray = True)
plt.imshow(img)