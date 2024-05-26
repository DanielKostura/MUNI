import cv2

# Function to convert bits to text
def bits_to_text(bits):
    # Join the bits into a single string
    bits_string = ''.join(bits)

    # Split the bits string into 8-bit chunks
    byte_strings = [bits_string[i:i+8] for i in range(0, len(bits_string), 8)]

    # Pad the last chunk with zeros on the left if it's less than 8 bits long
    byte_strings[-1] = byte_strings[-1].zfill(8)

    # Convert each 8-bit chunk to a character
    bytes = [int(byte_string, 2) for byte_string in byte_strings]

    # Convert the bytes to text using 'utf-8' with error handling
    text = bytearray(bytes).decode('utf-8', errors='replace')

    return text

# Load the image
image_path = "Ah3rIZDqZw.png"
img = cv2.imread(image_path)

# Function to extract LSBs from each channel and concatenate them
def extract_lsb(img):
    lsb_array = []
    for channel in cv2.split(img):
        lsb_channel = channel & 1  # Extract the least significant bit
        lsb_array.append(lsb_channel)

    return lsb_array

# Extract least significant bits
lsb_pixels = extract_lsb(img)

# Flatten the 2D array to a 1D array
lsb_bits = [str(pixel[0]) for row in lsb_pixels for pixel in row]

# Convert the bits to text using the provided bits_to_text function
decoded_text = bits_to_text(lsb_bits)

# Print the decoded text
print(decoded_text)
