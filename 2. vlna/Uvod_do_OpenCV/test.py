import cv2 as cv
import numpy as np

img = cv.imread("k.png", cv.IMREAD_COLOR)
nula_img = cv.flip(img, 0)
plus_img = cv.flip(img, 1)
minus_img = cv.flip(img, -1)
#resized_img = cv.resize(img, (1000, 1000))

"""
img = np.zeros((200,200,3), dtype=np.uint8)
color = np.array([0x33, 0xcc, 0x33], dtype=np.uint8)
img[:, :] = color
"""

cv.imshow("original", img)
cv.imshow("nula", nula_img)
cv.imshow("plus", plus_img)
cv.imshow("minus", minus_img)

cv.waitKey(0)
cv.destroyAllWindows()