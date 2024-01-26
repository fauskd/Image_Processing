from skimage import io

from skimage.filters import roberts, sobel, scharr, prewitt

import matplotlib.pyplot as plt


img = io.imread('/Users/sajalkumardas/Desktop/Image Processing/test_images/cropped_img.jpg', as_gray= True)

edged_roberts = roberts(img)
edged_sobel = sobel(img)
edged_scharr = scharr(img)
edged_prewitt = prewitt(img)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2, sharex = True,
                                             sharey = True, figsize = (8,8))


ax1.set_title('roberts')
ax1.imshow(edged_roberts, cmap = plt.cm.gray)

ax2.set_title('sobel')
ax2.imshow(edged_sobel, cmap = plt.cm.gray)

ax3.set_title('scharr')
ax3.imshow(edged_scharr, cmap = plt.cm.gray)

ax4.set_title('prewitt' )
ax4.imshow(edged_prewitt, cmap = plt.cm.gray)


from skimage.feature import canny
edged_canny = canny(img, sigma = 2)
plt.imshow(edged_canny)

plt.tight_layout()
plt.show()
