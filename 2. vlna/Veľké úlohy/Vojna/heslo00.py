import numpy, cv2

def text_to_bits(text):
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))

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

def extract_text(image_path, text_length):
    # Load the image
    img = cv2.imread(image_path)
    # Extract the bits
    bits = ""
    for i in range(text_length * 30 +40):
        # Find the pixel
        y = i // img.shape[1]
        x = i % img.shape[1]

        # Extract the least significant bit of the pixel's blue color
        bits += str(img[y, x, 0] & 0x1)

    # Convert the bits to text
    return bits_to_text(bits)


name = "iHC438uwRv"
text = "1. Načtěte zakódovaný obrázek. 2. Extrahujte bity. 3. Najděte pixely. Extrahujte LSB.4. Vraťte text."

a = extract_text(f"{name}.png", len(text.encode('utf-8')))
print(a)