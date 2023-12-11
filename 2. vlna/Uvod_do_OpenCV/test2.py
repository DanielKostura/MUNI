import cv2 as cv
import numpy as np

img = cv.imread("2. vlna/Uvod_do_OpenCV/ksi.png", cv.IMREAD_COLOR)

yellow_lower = np.array([48, 132, 189])
yellow_upper = np.array([64, 176, 252])

m = cv.inRange(img, yellow_lower, yellow_upper)
mask = cv.bitwise_not(cv.inRange(img, yellow_lower, yellow_upper))
#img = cv.bitwise_xor(img, mask)

cv.imshow("w", m)
cv.imshow("window_name", img)

cv.waitKey(0)
cv.destroyAllWindows() 