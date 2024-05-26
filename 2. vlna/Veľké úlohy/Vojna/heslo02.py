import numpy as np
import cv2 as cv

image_path = "wpwpGGs180noscope.png" # "iHC438uwRv.png" 

img = cv.imread(image_path)
final = np.zeros((len(img),len(img[0]),3), dtype=np.uint8) # 1.

print(img)
print(final)
for i in range(len(img)):
    for j in range(len(img[0])):
        if img[i, j, 2] % 2 == 0:
            final[i, j] = [255, 255, 255]

cv.imshow("final", final)
cv.waitKey(0)
cv.destroyAllWindows()


"""
1. Pro uložení dekódovaného obrázku se vytvoří prázdné pole stejné velikosti jako kódovaný obrázek.
2. Dekódování se provádí kontrolou bajtu červeného kanálu každého pixelu v zakódovaném obrázku.
   Pokud je bajt sudý, odpovídající pixel v dekódovaném obrázku je nastaven na bílou (255).
   Jinak bajt zůstane černý.
3. Dekódovaný obrázek se uloží do zadané výstupní cesty.
"""