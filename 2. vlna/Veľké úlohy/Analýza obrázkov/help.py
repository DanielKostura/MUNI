import cv2
import numpy as np

f = open("help-h.txt", "a")

def count_of_pix(img, lower_color, upper_color): # počitanie pixelov rôznej farby
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    cv2.imshow("w", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    pocet_pixelov = cv2.countNonZero(mask)

    return pocet_pixelov / (len(img) * len(img[0]) * len(img[0, 0])) * 100 # vyjadrenie pixelou podielom veľkosti obrázku aby bolo jedno aká je fotka veľká

def pixCount(img, color_lower, color_upper): # to iste ako count_of_pix ale postupom casu som prisiel na elegantnejsie riesenie
    mask = cv2.inRange(img, color_lower, color_upper)
    pocet_pixelov = cv2.countNonZero(mask)
    return round(pocet_pixelov/(len(img) * len(img[0])) * 100, 2)

def kategorizuj_obraz(image):
    brown_orange_pixs = round(count_of_pix(image, (0, 50, 50), (0, 255, 255)), 2) # (0, 50, 50), (0, 255, 255)
    white_pixs = round(count_of_pix(image, (150, 150, 150), (255, 255, 255)), 2) # (0, 0, 200), (180, 30, 255)
    green_pixs = round(count_of_pix(image, (40, 40, 40), (80, 255, 255)), 2) # (40, 40, 40), (80, 255, 255)

    print(f"{brown_orange_pixs}, {white_pixs}, {green_pixs}", file=f)

# Načítanie obrazu
print("jar_leto", file=f)
for i in range(1, 7):
    obraz = cv2.imread(f"public_tests/spring_summer/jar_leto{str(i)}.jpg")
    kategoria = kategorizuj_obraz(obraz)

print("jesen", file=f)
for i in range(1, 7):
    obraz = cv2.imread(f"public_tests/autumn/autumn{str(i)}.jpg")
    kategoria = kategorizuj_obraz(obraz)

print("zima", file=f)
for i in range(6):
    obraz = cv2.imread(f"public_tests/winter/winter{str(i)}.jpg")
    kategoria = kategorizuj_obraz(obraz)
    # print("Kategória obrazu:", kategoria)

f.close()