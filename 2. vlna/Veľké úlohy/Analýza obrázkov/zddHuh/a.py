import cv2
import numpy as np

def najcastejsia_farba_obrazku(obrazok_cesta, tolerancia=10):
    # Načítanie obrazu
    obrazok = cv2.imread(obrazok_cesta)

    # Prevedenie obrazu z BGR do RGB
    obrazok_rgb = cv2.cvtColor(obrazok, cv2.COLOR_BGR2RGB)

    # Získanie rozmernosti obrazu
    vyska, sirka, _ = obrazok_rgb.shape

    # Zmena tvaru obrazu na jednorozmerné pole
    obrazok_flatten = obrazok_rgb.reshape((vyska * sirka, 3))

    # Získanie četnosti farieb
    pocetnost_farieb = np.bincount(obrazok_flatten.argmax(axis=1))

    # Získanie indexu najčastejšej farby
    index_najcastejsiejsie_farby = pocetnost_farieb.argmax()

    # Získanie RGB hodnôt najčastejšej farby
    najcastejsia_farba = np.unravel_index(index_najcastejsiejsie_farby, (256, 256, 256))

    # Vytvorenie rozsahu pre najčastejšiu farbu s toleranciou
    lower_color = np.array([max(0, val - tolerancia) for val in najcastejsia_farba])
    upper_color = np.array([min(255, val + tolerancia) for val in najcastejsia_farba])

    return lower_color, upper_color

# Cesta k obrazu
print("jesen")
for i in range(1, 7):
    lower_color, upper_color = najcastejsia_farba_obrazku(f"public_tests/autumn/autumn{str(i)}.jpg", tolerancia=10)

    print(f"LC: {lower_color}, UC: {upper_color}")


print("jar_leto")
for i in range(1, 7):
    lower_color, upper_color = najcastejsia_farba_obrazku(f"public_tests/spring_summer/jar_leto{str(i)}.jpg", tolerancia=10)

    print(f"LC: {lower_color}, UC: {upper_color}")


print("zima")
for i in range(6):
    lower_color, upper_color = najcastejsia_farba_obrazku(f"public_tests/winter/winter{str(i)}.jpg", tolerancia=10)

    print(f"LC: {lower_color}, UC: {upper_color}")
