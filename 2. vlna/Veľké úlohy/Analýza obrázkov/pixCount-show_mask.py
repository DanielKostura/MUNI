import numpy as np
import cv2 as cv

f = open("help-g.txt", "a")

def pixCount(img, color_lower, color_upper):
    mask = cv.inRange(img, color_lower, color_upper) 
    pocet_pixelov = cv.countNonZero(mask)
    return round(pocet_pixelov/(len(img) * len(img[0])) * 100, 2)

def show_mask(img, color_lower, color_upper): 
    mask = cv.inRange(img, color_lower, color_upper)
 
    cv.imshow("img", img) 
    cv.imshow("mask", mask) 
    cv.waitKey(0)
    cv.destroyAllWindows()

#img_path = "karlik.png"
#img_path = "public_tests/winter/winter3.jpg"
#img = cv.imread(img_path, cv.IMREAD_COLOR)

        # B  G  R
lower = (20, 90, 55)#(0, 70, 110) #(20, 90, 55) #(185, 175, 150)
upper = (100, 150, 120) #(60, 160, 230) #(100, 1 50, 120) green #(255, 255, 225) white

sum = 0
print("jar_leto", file=f)
for i in range(1, 7):
    img = cv.imread(f"public_tests/spring_summer/jar_leto{str(i)}.jpg")
    #show_mask(img, lower, upper)

    print(pixCount(img, lower, upper), file=f)
    sum += pixCount(img, lower, upper)

print(sum/6)

sum = 0
print("jesen", file=f)
for i in range(1, 7):
    img = cv.imread(f"public_tests/autumn/autumn{str(i)}.jpg")
    #show_mask(img, lower, upper)
    print(pixCount(img, lower, upper), file=f)
    sum += pixCount(img, lower, upper)

print(sum/6)
 
sum = 0
print("zima", file=f)
for i in range(6):
    img = cv.imread(f"public_tests/winter/winter{str(i)}.jpg")
    #show_mask(img, lower, upper)
    print(pixCount(img, lower, upper), file=f)
    sum += pixCount(img, lower, upper)

print(sum/6)