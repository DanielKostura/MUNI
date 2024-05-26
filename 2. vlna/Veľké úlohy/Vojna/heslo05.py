import numpy as np
import cv2 as cv

def bits_to_text(bits):
    # Join the bits into a single string
    bits_string = ''.join(bits)

    # Split the bits string into 8-bit chunks
    byte_strings = [bits_string[i:i+8] for i in range(0, len(bits_string), 8)]

    # Pad the last chunk with zeros on the left if it's less than 8 bits long
    byte_strings[-1] = byte_strings[-1].zfill(8)

    # Convert each 8-bit chunk to a character
    bytes = [int(byte_string, 2) for byte_string in byte_strings]

    # Convert the bytes to text using 'utf-8'
    text = bytearray(bytes).decode('utf-8')

    return text

def decode_image(height, width):
    arr = []

    for i in range(height):
        for j in range(width):
            pole = []
            pole.append(img[i, j, 0] & 0b00000001)
            pole.append(img[i, j, 1] & 0b00000001)
            pole.append(img[i, j, 2] & 0b00000001)
            arr.append(pole)
    p = []
    for i in range(len(arr)):
        for j in range(3):
            p.append(arr[i][j])

    bits = ""
    for i in range(8*416):
        bits += str(p[i])

    return bits_to_text(bits)

image_path = "Y0urM0mL1k3sM1Lk.png" # "Ah3rIZDqZw.png"
img = cv.imread(image_path)
height, width, _ = img.shape
print(decode_image(height, width))

"""
original image => Alg03 -> image with code -> image => Alg04(Stejne heslo jako naposledy) -> 
code to next image => Alg02 -> image with code to next image -> image => Alg05 -> lastCode -> lastImage
"""