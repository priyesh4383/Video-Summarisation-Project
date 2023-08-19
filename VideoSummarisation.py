import cv2
import numpy as np

def detect_shot_boundaries(video_path, threshold):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get video frame count and first frame
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    _, prev_frame = cap.read()

    # Create empty list to store unique frames
    unique_frames = [prev_frame]

    frame_number=1
    # Iterate through frames and detect shot boundaries
    for i in range(1, frame_count):
        res, curr_frame = cap.read()
        if res:
            print(frame_number)
            frame_number+=1
            diff = cv2.absdiff(curr_frame, prev_frame)
            diff_mean = diff.mean()
            if diff_mean>threshold:
                unique_frames.append(curr_frame)
                
            prev_frame=curr_frame

    cap.release()

    # Write unique frames to output video file
    output_path = "ramp_test1.avi" # converting it to avi because XVID codec supports avi format better than mp4
    fourcc = cv2.VideoWriter_fourcc(*"XVID") 
    out = cv2.VideoWriter(output_path, fourcc, 30, (prev_frame.shape[1], prev_frame.shape[0])) # 30 is FPS - Hyperparameter

    for frame in unique_frames:
        out.write(frame)

    out.release()

# Example
video_path = "input1.mp4"
threshold = 2 # Hyperparameter
detect_shot_boundaries(video_path, threshold) # Finally applying the function to our custom video
