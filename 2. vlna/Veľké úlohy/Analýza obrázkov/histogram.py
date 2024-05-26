import cv2
import matplotlib.pyplot as plt

def generate_histogram(image_path):
    # Read the image
    img = cv2.imread(image_path, 0)  # 0 for grayscale, 1 for color
    cv2. imshow('image', img)
    # Calculate histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # Plot the histogram
    plt.plot(hist)
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

# Example usage
image_path = 'public_tests/sunrise_sunset/sunrise_sunset0.jpg'
generate_histogram(image_path)
image_path = 'public_tests/sunrise_sunset/sunrise_sunset1.jpg'
generate_histogram(image_path)
image_path = 'public_tests/sunrise_sunset/sunrise_sunset2.jpg'
generate_histogram(image_path)
image_path = 'public_tests/sunrise_sunset/sunrise_sunset3.jpg'
generate_histogram(image_path)
image_path = 'public_tests/sunrise_sunset/sunrise_sunset4.jpg'
generate_histogram(image_path)
image_path = 'public_tests/sunrise_sunset/sunrise_sunset5.jpg'
generate_histogram(image_path)


image_path = 'public_tests/midday/midday0.jpg'
generate_histogram(image_path)
image_path = 'public_tests/midday/midday1.jpg'
generate_histogram(image_path)
image_path = 'public_tests/midday/midday2.jpg'
generate_histogram(image_path)
image_path = 'public_tests/midday/midday3.jpg'
generate_histogram(image_path)
image_path = 'public_tests/midday/midday4.jpg'
generate_histogram(image_path)
image_path = 'public_tests/midday/midday5.jpg'
generate_histogram(image_path)


image_path = 'public_tests/night/night0.jpg'

image_path = 'public_tests/night/night1.jpg'

image_path = 'public_tests/night/night2.jpg'

image_path = 'public_tests/night/night3.jpg'

image_path = 'public_tests/night/night4.jpg'

image_path = 'public_tests/night/night5.jpg'


"""
generate_histogram(image_path)
"""

