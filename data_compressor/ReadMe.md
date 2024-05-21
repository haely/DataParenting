# Data Compressor

This project provides scripts to compress image, video, and text data. It includes three main Python scripts, each designed to handle a different type of data compression.

## Project Structure

data_compressor/
│
├── compress_image.py
├── compress_video.py
├── compress_text.py
├── requirements.txt
└── README.md


## Requirements

- Python 3.x
- Pillow
- OpenCV
- gzip (standard library)
- shutil (standard library)

To install the required packages, you can use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
## Usage

### Compress Image
The compress_image.py script compresses image files using the Pillow library. You can specify the input image, output path, and compression quality.

#### Example:

Update the input_path and output_path variables in compress_image.py with your desired file paths.

Run the script:
```python compress_image.py```

The compressed image will be saved to the specified output path.

### Compress Video
The compress_video.py script compresses video files using OpenCV. You can specify the input video, output path, codec, and bitrate.

#### Example:

Update the input_path and output_path variables in compress_video.py with your desired file paths.

Run the script:
`python compress_video.py`

The compressed video will be saved to the specified output path.

### Compress Text
The compress_text.py script compresses text files using gzip. You can specify the input text file and output path.

#### Example:

Update the input_path and output_path variables in compress_text.py with your desired file paths.

Run the script:
`python compress_text.py`

The compressed text file will be saved to the specified output path.

## File Descriptions

compress_image.py: Script to compress image files. Uses the Pillow library to save images with reduced quality.
compress_video.py: Script to compress video files. Utilizes OpenCV to re-encode videos with a specified codec and bitrate.
compress_text.py: Script to compress text files. Employs gzip for file compression.
requirements.txt: Lists the external Python packages required for the project.
README.md: Provides an overview of the project, setup instructions, and usage examples.
Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

