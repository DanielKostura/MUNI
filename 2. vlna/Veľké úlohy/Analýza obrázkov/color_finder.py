import numpy as np
import cv2 as cv

f = open("help-h.txt", "a")

def pixCount(img, color_lower, color_upper):
    mask = cv.inRange(img, color_lower, color_upper)
    pocet_pixelov = cv.countNonZero(mask)
    return round(pocet_pixelov/(len(img) * len(img[0])) * 100, 2)

def show_mask(img, color_lower, color_upper):
    mask = cv.inRange(img, color_lower, color_upper)

    cv.imshow("window_name", mask)
    cv.waitKey(0)
    cv.destroyAllWindows()

#img_path = "public_tests/winter/winter3.jpg"
#img = cv.imread(img_path, cv.IMREAD_COLOR)