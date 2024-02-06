import cv2

def load_image(image_path):
    try:
        # Load an image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Unable to load image at {image_path}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def resize_image(image, new_width=100):
    # Compute the ratio of the new width to the old width, and adjust height accordingly
    ratio = new_width / image.shape[1]
    new_height = int(image.shape[0] * ratio)
    return cv2.resize(image, (new_width, new_height))

def pixel_to_ascii(image):
    # Map grayscale values to ASCII characters
    ascii_chars = "@%#*+=-:. "
    new_image = []
    for row in image:
        new_image.append(''.join([ascii_chars[pixel//32] for pixel in row]))
    return "\n".join(new_image)

