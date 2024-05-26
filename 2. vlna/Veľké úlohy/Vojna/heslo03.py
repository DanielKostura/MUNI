import cv2 as cv
import numpy as np

def decode_image(image_path, k):
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

image_path = "p0078Px2z1.png"
a = decode_image(image_path, 0)
b = decode_image(image_path, 1)
c = decode_image(image_path, 2)

d = cv.bitwise_or(a, b)
e = cv.bitwise_or(d, c)

cv.imwrite("image10.jpg", e)

cv.imshow("e", e)
cv.waitKey(0)
cv.destroyAllWindows()

# 0 - H26
# 1 - rum /rUm
# 2 - 92cL

"""
1. Pro každý pixel v kódovaném obrázku extrahujte nejméně důležitý bit. (rada: image & 0b00000001)
2. Posuňte bity dekódovaného obrázku doleva o 7 míst. Díky tomu bude zpráva viditelná,
   když přesunete nejméně významný bit na pozici nejvýznamnějšího bitu.
3. Po zpracování všech pixelů uložte dekódovaný obrázek pomocí cv2.imwrite.
"""