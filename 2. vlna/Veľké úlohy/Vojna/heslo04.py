import cv2

def select_pixel(image, key, bit_index):
    key_value = sum(ord(char) for char in key) + bit_index
    x = key_value % image.shape[1]
    y = key_value // image.shape[1]
    pixel = image[y, x]
    return pixel

def decode_image(image_path, key):
    img = cv2.imread(image_path)

    message_length = len(key) * 8
    bits = []
    for bit_index in range(message_length*47+11):
        pixel = select_pixel(img, key, bit_index)
        blue_channel_lsb = pixel[0] & 1  # Extract the least significant bit of the blue channel
        bits.append(str(blue_channel_lsb))

    decoded_text = bits_to_text(bits)
    return decoded_text

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

# Example usage
image_path = "ALm0stTh3r3L1ttLe0n3.png" # "9rH2U2cm6L.png"
key = "LosKarlos"
decoded_message = decode_image(image_path, key)
print(decoded_message)

