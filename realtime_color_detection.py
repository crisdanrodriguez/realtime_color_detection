# Import libraries
import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

while True:

    # Reading the video from the webcam in image frames
    ret, frame = webcam.read()

    # Show the readed frames
    cv2.imshow('frame', frame)

    # Condition for finishing the video capture when pressing 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Program termination
webcam.release()
cv2.destroyAllWindows
