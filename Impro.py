import cv2
import glob
path = "Image Processing/test_images/*"

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    print(a)
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow("color_image", c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
