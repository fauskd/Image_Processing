from PIL import Image

img = Image.open('test_images/coffee.jpg')

img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save('test_images/leftright.jpg')

img_flipTB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipTB.save('test_images/topbottom.jpg')
