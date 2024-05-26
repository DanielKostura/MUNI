import numpy as np
import cv2 as cv

image_path = ""

img = cv.imread(image_path)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()