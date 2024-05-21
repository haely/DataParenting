import gzip
import shutil

def compress_text(input_file, output_file):
    """Compress a text file using gzip."""
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

if __name__ == "__main__":
    input_path = 'input_text.txt'  # Replace with your text file path
    output_path = 'compressed_text.txt.gz'  # Replace with desired output path
    compress_text(input_path, output_path)
    print(f"Text file saved to {output_path}")

