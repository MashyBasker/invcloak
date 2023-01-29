"""
Utility Program I: Program to demonstrate color segmentation

Author: Maharshi Basu
Date: 8 January, 2023

Description: This program is supposed to detect only the red color cloth in the frame and everything else
            should be black

"""

#importing the required libraries
import cv2
import numpy as np
from time import sleep

def color_segment(inp_frame):
    hsv_img = cv2.cvtColor(inp_frame, cv2.COLOR_BGR2HSV)        #converting the image to hsv format
    lower_yellow = np.array([25, 50, 70]) #60, 40.7, 99.2
    upper_yellow = np.array([35, 255, 255]) #60, 100, 100
    mask2 = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
    return mask2                                                 #returning the mask for segmenting the image

cap = cv2.VideoCapture(0)                                       #starting webcam
sleep(1)                                                        #giving a second for the code to access the webcam

while cap.isOpened():
    _, frame = cap.read()                                       #reading each frame from the video
    mask = color_segment(frame)                                 #using utility function to generate the mask

    res = cv2.bitwise_and(frame, frame, mask=mask)              #applying the mask
    res1 = cv2.bitwise_not(res)                                 #inverting the mask
    res2 = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Red segment", res2)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


