from PIL import Image
img = Image.open('monalisa.jpg')
print(img)
print(img.format)
print(img.size)
small_img = img.resize((200,200))
small_img.save('test_images/resize.jpg')
print(small_img.size)

#thumbnail is not accepting the size while it is more that it's original size
img.thumbnail((500,700))
img.save("test_images/thumbnail.jpg")
print(img.size)

#crop a picture
cropped_img = img.crop((0,0, 150,150))
cropped_img.save("test_images/cropped_img.jpg")