import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8s.pt")  # Ensure this file downloads automatically if not present

# Speed estimation function using Optical Flow
def estimate_speed(prev_gray, curr_gray):
    flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 
                                        0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    return np.mean(magnitude)

# Input and Output video paths
input_video = "input_video.mp4"  # Replace with your video file
output_video = "output_video.mp4"

# Load video
cap = cv2.VideoCapture(input_video)

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video.")
    exit()

# Read first frame for optical flow initialization
ret, prev_frame = cap.read()
if not ret:
    print("Error reading the first frame.")
    cap.release()
    exit()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Define video writer to save annotated output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, 30, 
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
                       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

# Process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detection for vehicles, obstacles, potholes
    results = model(frame, conf=0.5)
    annotated_frame = results[0].plot()

    # Convert current frame to grayscale for speed estimation
    curr_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Estimate speed using optical flow
    if prev_gray is not None:
        avg_speed = estimate_speed(prev_gray, curr_gray)
        cv2.putText(annotated_frame, f"Approach Speed: {avg_speed:.2f} px/frame",
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write frame to output video
    out.write(annotated_frame)

    # Optional visualization using matplotlib (skip for large videos)
    # plt.imshow(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
    # plt.axis('off')
    # plt.show()

    prev_gray = curr_gray

cap.release()
out.release()
print("Processing complete. Output video saved.")

