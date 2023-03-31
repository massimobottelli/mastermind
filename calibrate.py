import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the mouse callback function
def mouse_callback(event, x, y, flags, params):
    global x_init, y_init, drawing, frame

    # If the left mouse button is pressed, record the initial position of the rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        x_init, y_init = x, y
        drawing = True

    # If the left mouse button is released, stop recording the rectangle and extract the HSV values
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        # Extract the rectangle coordinates and dimensions
        x_min, y_min = min(x_init, x), min(y_init, y)
        x_max, y_max = max(x_init, x), max(y_init, y)
        w, h = x_max - x_min, y_max - y_min

        # Extract the ROI from the frame and convert it to HSV
        roi = frame[y_min:y_min+h, x_min:x_min+w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Extract the highest and lowest HSV values in the ROI
        h_max, s_max, v_max = np.amax(hsv_roi, axis=(0, 1))
        h_min, s_min, v_min = np.amin(hsv_roi, axis=(0, 1))

        # Print the highest and lowest HSV values

        print (f"'color': (({h_min},{s_min},{v_min}), ({h_max},{s_max},{v_max})),")

        # Draw the rectangle on the frame
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

# Initialize the drawing variable and the initial position of the rectangle
drawing = False
x_init, y_init = 0, 0

# Create a window and set the mouse callback function
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_callback)

# Loop through each frame from the webcam
while True:
    # Read the frame
    ret, frame = cap.read()

    # Show the frame
    frame = cv2.resize(frame, (800, 480))
    cv2.imshow('frame', frame)

    # Check for key presses
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close the preview window
cap.release()
cv2.destroyAllWindows()
