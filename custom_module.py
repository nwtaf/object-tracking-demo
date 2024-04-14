import cv2

def extract_center_coordinates(xywh_temp, id_temp, desired_track_id):
    """
    Extracts the center coordinates from the given bounding box coordinates for a specific track ID.

    Args:
        xywh_temp (tensor): 2D tensor of bounding box coordinates in the format [x, y, width, height].
        id_temp (tensor): 1D tensor of track IDs.
        desired_track_id (float): The track ID for which to extract the center coordinates.

    Returns:
        tuple: A tuple of ints containing the center coordinates (center_x, center_y) for the desired track ID.
    """
    for track_id, box in zip(id_temp, xywh_temp):
        if track_id == desired_track_id:
            center_x, center_y, width, height = box
            print(f'desired_track_id: {desired_track_id}, center_x: {center_x}, center_y: {center_y}, width: {width}, height: {height}')
            center_x = int(center_x)
            center_y = int(center_y)
            return (center_x, center_y)
    return None

def plot_center_on_frame(frame, center_coordinates):
    """
    Plot the center coordinates on the given frame.

    Args:
        frame (numpy.ndarray): The image frame on which to plot the center coordinates.
        center_coordinates (int(tuple)): The coordinates of the center point.

    Returns:
        The modified frame with the center coordinates plotted.
    """
    # Plot the center on the image
    radius = 10  # Radius of the circle
    color = (0, 255, 0)  # Red color
    thickness = -1  # Thickness
    frame = cv2.circle(frame, (center_coordinates), radius, color, thickness)
    return frame

def resize_frame(frame, desired_width):
    """
    Resize the given frame to the specified width.

    Args:
        frame (numpy.ndarray): The image frame to resize.
        width (int): The width to resize the frame to.

    Returns:
        The resized frame.
    """
    height, width, _ = frame.shape
    aspect_ratio = width / height
    new_height = int(desired_width / aspect_ratio)
    resized_frame = cv2.resize(frame, (desired_width, new_height))
    return resized_frame

# if script is being run as main module
if __name__ == "__main__":
    from ultralytics import YOLO

    model = YOLO('yolov8n.pt') # load model
    results = model.track(source='data/gremlin.jpg', show=False)

    xywh_temp = results[0].boxes.xywh
    id_temp = results[0].boxes.id
    cx, cy = extract_center_coordinates(xywh_temp, id_temp, 1) # id cannot be zero
    annotated_frame = plot_center_on_frame(results[0].plot(), (cx, cy))
    annotated_frame = resize_frame(annotated_frame, 420)
    cv2.imshow('Annotated Frame', annotated_frame)
    cv2.waitKey(0)
    