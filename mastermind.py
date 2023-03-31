import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the lower and upper bounds for each color in HSV format
colors = {
    'red': ((0, 100, 100), (20, 255, 255)),
    'green': ((36, 25, 25), (86, 255, 255)),
    'blue': ((100, 50, 50), (130, 255, 255)),
    'yellow': ((20, 100, 100), (30, 255, 255)),
    'orange': ((10, 100, 100), (20, 255, 255)),
    'purple': ((125, 50, 50), (150, 255, 255))
}

# Initialize the detected colors array
detected_colors = []

# Loop through each frame from the webcam
while True:
    # Read the frame
    ret, frame = cap.read()

    # Convert the frame to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect the colored rectangles
    for color, (lower, upper) in colors.items():
        # Create a mask for the color
        mask = cv2.inRange(hsv, lower, upper)

        # Find the contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop through each contour
        for contour in contours:
            # Get the area and perimeter of the contour
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)

            # Approximate the contour to a polygon
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

            # Check if the polygon is a rectangle
            if len(approx) == 4:
                # Check if the rectangle is larger than 100x100 pixels
                x, y, w, h = cv2.boundingRect(approx)
                if w > 100 and h > 100:
                    # Draw the rectangle on the frame
                    cv2.drawContours(frame, [approx], -1, (255, 0, 0), 2)
                    # Write the color name above the rectangle
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                    # Get the color of the rectangle
                    if color not in detected_colors:
                        detected_colors.append(color)

    # Show the frame
    frame = cv2.resize(frame, (800, 480))
    cv2.imshow('Mastermind', frame)

    # Check for key presses
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close the preview window
cap.release()
cv2.destroyAllWindows()


# Print the color array
print(detected_colors)
