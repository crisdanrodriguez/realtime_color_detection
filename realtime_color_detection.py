# Import libraries
import numpy as np
import cv2

def trackbar_changed(x):
    pass

# Set trackbar window name
cv2.namedWindow('Color Track Bar')

# Initialize trackbar limits for HSV color space
low_H = 112
high_H = 112

low_S = 112
high_S = 255

low_V = 112
high_V = 255

# Create trackbar for HSV color change
cv2.createTrackbar('Low H', 'Color Track Bar', low_H, 255, trackbar_changed)
cv2.createTrackbar('High H', 'Color Track Bar', high_H, 255, trackbar_changed)

cv2.createTrackbar('Low S', 'Color Track Bar', low_S, 255, trackbar_changed)
cv2.createTrackbar('High S', 'Color Track Bar', high_S, 255, trackbar_changed)

cv2.createTrackbar('Low V', 'Color Track Bar', low_V, 255, trackbar_changed)
cv2.createTrackbar('High V', 'Color Track Bar', high_V, 255, trackbar_changed)

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

while True:
    # Get trackbar values
    low_H = cv2.getTrackbarPos('Low H', 'Color Track Bar')
    high_H = cv2.getTrackbarPos('High H', 'Color Track Bar')

    low_S = cv2.getTrackbarPos('Low S', 'Color Track Bar')
    high_S = cv2.getTrackbarPos('High S', 'Color Track Bar')

    low_V = cv2.getTrackbarPos('Low V', 'Color Track Bar')
    high_V = cv2.getTrackbarPos('High V', 'Color Track Bar')

    # Reading the video from the webcam in image frames
    ret, frame = webcam.read()

    # Convert the image frame in BGR to HSV color space
    hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Set ranges from trackbar selections
    lower_hsv = np.array([low_H, low_S, low_V])
    higher_hsv = np.array([high_H, high_S, high_V])

    # Set mask
    mask = cv2.inRange(hsvframe, lower_hsv, higher_hsv)

    # Show the real video and the mask
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # Condition for finishing the video capture when pressing 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Program termination
webcam.release()
cv2.destroyAllWindows
