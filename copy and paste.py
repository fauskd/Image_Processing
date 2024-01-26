from PIL import Image
img1 = Image.open('test_images/coffee.jpg')
print(img1.size)
img2 = Image.open('monalisa.jpg')
print(img2.size)
img2.thumbnail((100, 200))
img_copy = img1.copy()
img_copy.paste(img2, (200,200))
img_copy.save("test_images/new_image.jpg")
