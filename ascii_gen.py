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

def resize_image(image, new_height=100):
    # Calculate original ratio:
    original_height=image.shape[0]
    print(f'orig. height: {original_height}')
    original_width = image.shape[1]
    print(f'orig. height: {original_width}')
    ratio = original_width / original_height
    print(f'RATIO: {ratio}')
    
    # Calculate new height using ratio and new_width:
    new_width = int(new_height * ratio)
    print(f'New width: {new_width}')
    
    return cv2.resize(image, (new_height, new_width))


def pixel_to_ascii(image):
    # Map grayscale values to ASCII characters
    ascii_chars = "@%#*+=-:. "
    new_image = []
    for row in image:
        new_image.append(''.join([ascii_chars[pixel//32] for pixel in row]))
    return "\n".join(new_image)

