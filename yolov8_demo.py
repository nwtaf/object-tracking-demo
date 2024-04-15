'''
This script uses the Ultralytics YOLOv8 model to perform object detection on a video file, and then tracks the detected objects across frames. 
The script records the processing times for each frame, and creates graphs of the processing times and confidence values over time. 
The script uses a specified tracker configuration file, which is optimized for tracking objects across frames. 
The script saves the graphs to the 'data/graphs' directory.
'''
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import custom_module as cm

model = YOLO('yolov8n.pt') # load model
tracker = 'botsort' # 'bytetrack' 
video_path = 'data/hike.mp4' # 0

# Initialize variables
frame_count = 0

# conf_list[]
# cls_list[]
# id_list[]
# xywh_list[]
preprocess_time_list = []
inference_time_list = []
postprocess_time_list = []
total_processing_time_list = []
confidence_list = []

# Open the video file or camera 0
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
        raise ValueError("Failed to open the video path or capture device")
print('Video path successfully loaded')

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames.
        results = model.track(source=frame, persist=True, classes=[0], tracker=str(f'{tracker}.yaml'), verbose=False)

        # Access the returned results object; https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes
        # conf_temp = results[0].boxes.conf # class values
        # cls_temp = results[0].boxes.cls # confidence values
        id_temp = results[0].boxes.id # track IDs (if available)
        xywh_temp = results[0].boxes.xywh # boxes in xywh format; xywhn, xyxy, xyxyn are also available

        # Record times and confidence and increment frame count
        preprocess_time_list.append(results[0].speed['preprocess'])
        inference_time_list.append(results[0].speed['inference'])
        postprocess_time_list.append(results[0].speed['postprocess'])  
        total_processing_time_list.append(results[0].speed['preprocess'] + results[0].speed['inference'] + results[0].speed['postprocess'])
        confidence_list.append(results[0].boxes.conf)
        frame_count += 1
       
        # Visualize the results on the frame
        annotated_frame = cm.plot_center_on_frame(results[0].plot(), cm.extract_center_coordinates(xywh_temp, id_temp, 1))
        cv2.imshow("YOLOv8 Tracking", cm.resize_frame(annotated_frame, 640))

        # Break the loop if 'q' is pressed or if the display window is closed
        if cv2.waitKey(1) & 0xFF == ord("q") or cv2.getWindowProperty("YOLOv8 Tracking", cv2.WND_PROP_VISIBLE) < 1:
            break
    else:
        # Break the loop if the end of the video is reached
        break

cap.release()
cv2.destroyAllWindows()

# Calculate some averages
average_total_processing_time = np.mean(total_processing_time_list[1:])
average_confidence = np.mean(confidence_list[1:])
print(f"\nAverage Total Processing Time: {average_total_processing_time}")
print(f"Average Confidence: {average_confidence}")

# Create a graph of processing times vs frames, skipping first frame, #either show xor save, not both
plt.figure()
plt.plot(range(1, frame_count), total_processing_time_list[1:], label='Total Processing Time')
plt.plot(range(1, frame_count), preprocess_time_list[1:], label='Preprocess Time')
plt.plot(range(1, frame_count), inference_time_list[1:], label='Inference Time')
plt.plot(range(1, frame_count), postprocess_time_list[1:], label='Postprocess Time')

# # Create the directory if it doesn't exist
# path = Path("data/graphs/bookworm8GB/")
# if not path.exists():
#     path.mkdir(parents=True)

plt.xlabel('Frames')
plt.ylabel('Processing Times')
plt.title(f'{tracker.capitalize()}: Processing Times vs Frames')
plt.legend()
plt.savefig(f'data/graphs/{tracker}_total_processing_times_graph.png')
plt.close()

# Create a graph of confidence vs frames, skipping first frame
plt.figure()
plt.plot(range(1, frame_count), confidence_list[1:], label='Confidence')
plt.xlabel('Frames')
plt.ylabel('Confidence')
plt.title(f'{tracker.capitalize()}: Tracking Confidence vs Frames')
plt.legend()
plt.savefig(f'data/graphs/{tracker}_confidence_graph.png')
plt.close()