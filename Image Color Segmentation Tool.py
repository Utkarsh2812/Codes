import cv2
import numpy as np
import matplotlib.pyplot as plt

def on_trackbar_update(_):
    # Get the current trackbar positions
    h_min = cv2.getTrackbarPos('Hue Min', 'Segmentation')
    h_max = cv2.getTrackbarPos('Hue Max', 'Segmentation')
    s_min = cv2.getTrackbarPos('Saturation Min', 'Segmentation')
    s_max = cv2.getTrackbarPos('Saturation Max', 'Segmentation')
    v_min = cv2.getTrackbarPos('Value Min', 'Segmentation')
    v_max = cv2.getTrackbarPos('Value Max', 'Segmentation')

    # Create the lower and upper threshold arrays
    lower_threshold = np.array([h_min, s_min, v_min])
    upper_threshold = np.array([h_max, s_max, v_max])

    # Apply thresholding
    mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)
    segmented = cv2.bitwise_and(rgb_image, rgb_image, mask=mask)

    # Display segmented image
    cv2.imshow('Segmented Image', segmented)

# Load the image
image = cv2.imread('Thresh_segmentation.png')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window for segmentation
cv2.namedWindow('Segmentation')

# Create trackbars for threshold adjustment
cv2.createTrackbar('Hue Min', 'Segmentation', 0, 255, on_trackbar_update)
cv2.createTrackbar('Hue Max', 'Segmentation', 255, 255, on_trackbar_update)
cv2.createTrackbar('Saturation Min', 'Segmentation', 0, 255, on_trackbar_update)
cv2.createTrackbar('Saturation Max', 'Segmentation', 255, 255, on_trackbar_update)
cv2.createTrackbar('Value Min', 'Segmentation', 0, 255, on_trackbar_update)
cv2.createTrackbar('Value Max', 'Segmentation', 255, 255, on_trackbar_update)

# Initialize the trackbar callback to apply initial segmentation
on_trackbar_update(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
