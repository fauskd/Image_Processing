from PIL import Image
import glob


path = "images/*"

for file in glob.glob(path):
    print(file)
    a = Image.open(file)
    rotate45 = a.rotate(45, expand = True)
    rotate45.save(file+"rotated45.png", "PNG")