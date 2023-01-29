import cv2
import numpy as np
import matplotlib.pyplot as plt 

# read the image
img = cv2.imread('../assets/blue_flower.jpg')
# converting to HSV format
blur = cv2.blur(img, (5,5))
blur0 = cv2.medianBlur(blur, 5)
blur1 = cv2.GaussianBlur(blur0, (5,5), 0)
blur2 = cv2.bilateralFilter(blur1, 9, 75, 75)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_blue = np.array([110, 50, 50])
high_blue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, low_blue, high_blue)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite('../assets/blue_segmented_flower.png', res)
cv2.imshow("segmented flower", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

