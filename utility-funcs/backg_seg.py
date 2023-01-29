import cv2
import numpy as np
# from time import sleep
from color_seg import color_segment

cap = cv2.VideoCapture(0)

for i in range(100):
    _, backg = cap.read()


while cap.isOpened():
    _, frame = cap.read()
    mask = color_segment(frame)
    res = cv2.bitwise_and(frame, frame, mask=mask)              #applying the mask
    # res1 = cv2.bitwise_not(res)                               #inverting the mask
    # res2 = cv2.bitwise_and(frame, frame, mask=mask)
    res3 = cv2.bitwise_and(backg, backg, res, mask=mask)
    cv2.imshow("Background segmentation", res3)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()