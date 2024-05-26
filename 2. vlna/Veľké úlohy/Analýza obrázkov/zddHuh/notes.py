import cv2
import numpy as np

def detect_school_notes(image):
    # Preddefinované hodnoty pre farbu a tvar školských poznámok
    lower_color = np.array([100, 100, 100], dtype=np.uint8)
    upper_color = np.array([200, 200, 200], dtype=np.uint8)

    # Konverzia obrázka na formát HSV (Hue, Saturation, Value)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Maska pre farbu školských poznámok
    mask = cv2.inRange(hsv_image, lower_color, upper_color)

    # Hľadanie kontúr na maske
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Detekcia, či existujú nejaké kontúry (školské poznámky)
    if len(contours) > 0:
        return True  # Obrázok obsahuje školské poznámky
    else:
        return False  # Obrázok neobsahuje školské poznámky

# Príklad použitia
image_path = 'public_tests/not_notes/city1.JPG'
image = cv2.imread(image_path)

if detect_school_notes(image):
    print("Obrázok obsahuje školské poznámky.")
else:
    print("Obrázok neobsahuje školské poznámky.")
