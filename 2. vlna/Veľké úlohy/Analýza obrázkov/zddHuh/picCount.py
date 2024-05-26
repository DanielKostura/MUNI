import cv2

def pocet_farbenych_pixelov(image_path):
    # Nacítaj obrázok
    img = cv2.imread(image_path)

    # Konvertuj BGR na HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definuj rozsah farieb v HSV
    lower_yellow = (20, 100, 100)
    upper_yellow = (30, 255, 255)

    lower_orange = (10, 100, 100)
    upper_orange = (20, 255, 255)

    lower_yelloworange = (10, 100, 100)
    upper_yelloworange = (30, 255, 255)

    # Vytvor masku pre žltú farbu
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Vytvor masku pre oranžovú farbu
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)

    # Vytvor masku pre žltooranžovú farbu
    mask_yelloworange = cv2.inRange(hsv, lower_yelloworange, upper_yelloworange)

    # Spoj všetky masky
    combined_mask = mask_yellow + mask_orange + mask_yelloworange

    # Spočítaj počet farbených pixelov
    pocet_pixelov = cv2.countNonZero(combined_mask)

    return pocet_pixelov / (len(img)*len(img[0])*3)*100

# Použitie funkcie
image_path = 'public_tests/sunrise_sunset/sunrise_sunset0.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/sunrise_sunset/sunrise_sunset1.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/sunrise_sunset/sunrise_sunset2.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/sunrise_sunset/sunrise_sunset3.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/sunrise_sunset/sunrise_sunset4.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/sunrise_sunset/sunrise_sunset5.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

print("midday")
image_path = 'public_tests/midday/midday0.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/midday/midday1.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/midday/midday2.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/midday/midday3.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/midday/midday4.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

image_path = 'public_tests/midday/midday5.jpg'
pocet_pixelov = pocet_farbenych_pixelov(image_path)
print(f'Počet farbených pixelov: {pocet_pixelov}')

