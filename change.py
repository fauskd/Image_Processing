from skimage import io, img_as_ubyte

img = img_as_ubyte(io.imread('monalisa.jpg', as_gray = True))

print(img.shape, img.dtype)

print(img[0,0])

mean_value = img.mean()
max_value = img.max()
min_value = img.min()

print("the mean, max and min value are: ", mean_value, max_value, min_value)