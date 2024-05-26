import cv2 as cv
import numpy as np

def decode_image03(image_path, k):
    # Načtení obrázku
    img = cv.imread(image_path)

    # Získání rozměrů obrázku
    height, width, _ = img.shape

    # Inicializace pole pro dekódovaný obrázek
    decoded_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Procházení všech pixelů obrázku
    for i in range(height):
        for j in range(width):
            # Extrahování nejméně významného bitu
            lsb = img[i, j, k] & 0b00000001
            
            # Posunutí bitů doleva o 7 míst
            decoded_pixel_value = lsb << 7
            
            # Nastavení hodnoty pixelu v dekódovaném obrázku
            decoded_image[i, j] = [decoded_pixel_value, decoded_pixel_value, decoded_pixel_value]

    return decoded_image

image_path = "uWukiLW032.png"
a = decode_image03(image_path, 0)

cv.imshow("w", a)
cv.waitKey(0)
cv.destroyAllWindows()
# cv.imwrite("fromAlg03.jpg", a)

"""
original image 
=> Alg03 -> image with code -> image 
=> Alg04(Stejne heslo jako naposledy) -> code to next image 
=> Alg02 -> image with code to next image -> image 
=> Alg05 -> lastCode -> lastImage
"""