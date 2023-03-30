# mastermind

In this script, we first initialize the webcam using the cv2.VideoCapture function. We then define the lower and upper bounds for each color in HSV format. The HSV color space is used because it is more suitable for color detection than the RGB color space.

Next, we loop through each frame from the webcam. For each frame, we convert it to the HSV format and then detect the colored rectangles using the cv2.inRange and cv2.findContours functions. We then loop through each contour and check if it is a rectangle using the cv2.approxPolyDP function. If a rectangle is detected, we draw it on the frame using the cv2.drawContours function and display its color using the cv2.putText function.

Finally, we show the frame in a preview window using the cv2.imshow function and check for key presses using the `cv2.waitKey function. If the 'q' key is pressed, we break out of the loop and release the webcam using the cap.release function and close the preview window using the cv2.destroyAllWindows function.

To run this script, save it as a Python file and run it in your terminal or command prompt. Make sure you have the OpenCV library installed in your Python environment.

Note that the script assumes that the rectangles are placed side by side and do not overlap. If the rectangles overlap, the script may detect them as a single contour and not as separate rectangles.

Also, the color detection may not be perfect in all lighting conditions. You may need to adjust the lower and upper bounds for each color to get better results.

## Install OpenCV on Raspberry Pi

https://raspberrypi-guide.github.io/programming/install-opencv
