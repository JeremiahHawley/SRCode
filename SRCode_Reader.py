import os
from PIL import Image

# Specify the path to the PNG file
file_path = "test.png"

# Open the image
image = Image.open(file_path)

# Get the width and height of the image
width, height = image.size

# Get the image mode
mode = image.mode

# Iterate through the pixels and print the values
for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x, y))
        if mode == "RGB" or mode == "RGBA":
            r, g, b = pixel_value
            print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")
        elif mode == "L":
            gray_value = pixel_value
            print(f"Pixel at ({x}, {y}): Gray={gray_value}")
        else:
            print(f"Pixel at ({x}, {y}): {pixel_value}")