from PIL import Image
import os
import subprocess

def compress_png(input_file, output_file):
    """Compress a PNG image by optimizing it."""
    # Open the input image
    with Image.open(input_file) as img:
        img.save(output_file, "PNG", optimize=True)

    # Use optipng to further compress the PNG file
    subprocess.run(["optipng", "-o7", output_file])

    # Print file sizes for comparison
    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
    print(f"Original size: {original_size / 1024:.2f} KB")
    print(f"Compressed size: {compressed_size / 1024:.2f} KB")

if __name__ == "__main__":
    input_path = 'input_image.png'  # Replace with your image path
    output_path = 'compressed_image.png'  # Replace with desired output path
    compress_png(input_path, output_path)
    print(f"Image saved to {output_path}")

