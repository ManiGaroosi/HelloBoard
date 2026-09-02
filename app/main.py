from image_processing.preprocessing import (
    load_image,
    to_grayscale,
    apply_gaussian_blur,
    detect_edges,
)


def main():
    image = load_image("data/raw/pcb.jpg")

    gray = to_grayscale(image)

    blurred = apply_gaussian_blur(gray)

    edges = detect_edges(blurred)


if __name__ == "__main__":
    main()
