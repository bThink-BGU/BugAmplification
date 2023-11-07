import cv2
import os


def write_y4m_header(output_file, width, height, fps):
    header = f"YUV4MPEG2 W{width} H{height} F{fps}/1 Ip A1:1 C420\n"
    with open(output_file, "wb") as file:
        file.write(header.encode("utf-8"))


def save_y4m_frame(output_file, frame_data):
    # Append Y4M frame header
    with open(output_file, "ab") as file:
        header = f"FRAME\n"
        file.write(header.encode("utf-8"))

    # Append Y4M frame data
    with open(output_file, "ab") as file:
        file.write(frame_data)


def convert_mp4_to_y4m_and_save(input_file, num_frames_to_save):
    try:
        cap = cv2.VideoCapture(input_file)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = cap.get(5)

        output_file = os.path.splitext(input_file)[0] + ".y4m"

        write_y4m_header(output_file, frame_width, frame_height, int(fps))

        num_frames_to_save = min(num_frames_to_save, int(cap.get(7)) // 3)

        for i in range(num_frames_to_save):
            ret, frame = cap.read()
            if not ret:
                break

            frame_data = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV_I420).tobytes()
            save_y4m_frame(output_file, frame_data)

        cap.release()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    input_file = "D:/Yeshayahu/Temp/VID-20180502-WA0014.mp4"  # Replace with your input file
    num_frames = 100  # Adjust the number of frames as needed

    convert_mp4_to_y4m_and_save(input_file, num_frames)
