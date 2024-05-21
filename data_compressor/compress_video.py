import cv2

def compress_video(input_file, output_file, codec='XVID', bitrate='500k'):
    """Compress a video file to a specified bitrate."""
    cap = cv2.VideoCapture(input_file)
    fourcc = cv2.VideoWriter_fourcc(*codec)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()

if __name__ == "__main__":
    input_path = 'input_video.mp4'  # Replace with your video path
    output_path = 'compressed_video.mp4'  # Replace with desired output path
    compress_video(input_path, output_path)
    print(f"Video saved to {output_path}")

