from skimage import io
import matplotlib.pyplot as plt
import numpy as np

from skimage.filters.rank import entropy
from skimage.filters import threshold_otsu
from skimage.morphology import disk

img = io.imread('/Users/sajalkumardas/Desktop/Image Processing/monalisa.jpg')

plt.imshow(img)

entropy_img = entropy(img, disk(3))

plt.imshow(entropy_img)