import numpy as np
import cv2 as cv

f = open("notes.txt", "a")

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

        # B    G    R
lower = (120, 140, 150)
upper = (255, 255, 255) #white

sum = 0
print("notes", file=f)
for i in range(6):
    img = cv.imread(f"public_tests/notes/notes{str(i)}.jpg")
    show_mask(img, lower, upper)

    print(pixCount(img, lower, upper), file=f)
    sum += pixCount(img, lower, upper)

print(sum/6)

img = cv.imread(f"public_tests/not_notes/city1.jpg")
show_mask(img, lower, upper)
print(pixCount(img, lower, upper), file=f)
sum += pixCount(img, lower, upper)


img = cv.imread(f"public_tests/not_notes/midday2.JPG")
show_mask(img, lower, upper)
print(pixCount(img, lower, upper), file=f)
sum += pixCount(img, lower, upper)


img = cv.imread(f"public_tests/not_notes/nature3.jpg")
show_mask(img, lower, upper)
print(pixCount(img, lower, upper), file=f)
sum += pixCount(img, lower, upper)


img = cv.imread(f"public_tests/not_notes/nature4.jpg")
show_mask(img, lower, upper)
print(pixCount(img, lower, upper), file=f)
sum += pixCount(img, lower, upper)


img = cv.imread(f"public_tests/not_notes/night2.jpg")
show_mask(img, lower, upper)
print(pixCount(img, lower, upper), file=f)
sum += pixCount(img, lower, upper)

img = cv.imread(f"public_tests/not_notes/white_wall.jpg")
show_mask(img, lower, upper)
print(pixCount(img, lower, upper), file=f)
sum += pixCount(img, lower, upper)