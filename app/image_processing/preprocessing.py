import cv2


def load_image(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")

    return image


def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)


def detect_edges(image, threshold1=50, threshold2=150):
    return cv2.Canny(image, threshold1, threshold2)
