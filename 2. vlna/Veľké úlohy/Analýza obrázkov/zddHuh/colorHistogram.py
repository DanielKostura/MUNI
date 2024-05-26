import cv2
import matplotlib.pyplot as plt

# Načítanie obrazu

def histogram(image):
    # Prevod obrazu do formátu RGB (OpenCV načíta obraz v BGR)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Rozdelenie obrazu na farebné kanály
    channels = cv2.split(image_rgb)

    # Konfigurácia histogramu
    histSize = 256  # Počet binov
    histRange = (0, 256)  # Rozsah hodnôt
    hist_c = [cv2.calcHist([chan], [0], None, [histSize], histRange) for chan in channels]

    # Vytvorenie farebného histogramu
    colors = ('r', 'g', 'b')
    for hist, color in zip(hist_c, colors):
        plt.plot(hist, color=color)

    plt.title('Farebný Histogram')
    plt.xlabel('Hodnota pixelu')
    plt.ylabel('Počet pixelov')
    plt.show()

print("jesen")
for i in range(1, 7):
    obraz = cv2.imread(f"public_tests/autumn/autumn{str(i)}.jpg")
    kategoria = histogram(obraz)


print("jar_leto")
for i in range(1, 7):
    obraz = cv2.imread(f"public_tests/spring_summer/jar_leto{str(i)}.jpg")
    kategoria = histogram(obraz)


print("zima")
for i in range(6):
    obraz = cv2.imread(f"public_tests/winter/winter{str(i)}.jpg")
    kategoria = histogram(obraz)
    # print("Kategória obrazu:", kategoria)