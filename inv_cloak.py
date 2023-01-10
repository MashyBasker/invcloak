#importing the required libraries
import cv2
import numpy as np
from time import sleep

############################ PART I: CAPTURING THE BACKGROUND ########################################################

vid_cap = cv2.VideoCapture(0)     #to capture the video through webcam
sleep(1)                          #to provide some time for the code to access the camera

#to capture the background properly
#if just a single frame is provided, the frame comes out to be very dark
#providing some time, results in better frame data
for i in range(100):
    retval, backg = vid_cap.read()
    if retval == False:
        continue
#####################################################################################################################


########################### PART II: SEGMENTING THE COLOR FROM THE IMAGE FRAME ######################################
def color_segment(inp_frame):
    """Perform Color Segmentation from image frame. This function segments red color"""
    hsv_img = cv2.cvtColor(inp_frame, cv2.COLOR_BGR2HSV)        #converting the image to hsv format
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv_img, lower_red, upper_red)

    lower_red = np.array([170,120,70])                          #the HSV lower range for the color red
    upper_red = np.array([180, 255, 255])                       #the HSV upper range for the color red
    mask2 = cv2.inRange(hsv_img, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask2)
    return mask1, mask2                                                #returning the mask for segmenting red color
#####################################################################################################################

########################## PART III: ADD THE SEGMENTED BACKGROUND AND THE ORIGINAL IMAGE FRAME #######################
def invisibility_effect(frame, mask1, mask2, background):
    """Creates invisibility effect by adding the segmented background and the original image"""
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)
    output = cv2.addWeighted(res1, 1, res2, 1, 0)
    return output
#####################################################################################################################

########################################### MAIN FUNCTION ###########################################################
def main():
    while vid_cap.isOpened():
        _, frame = vid_cap.read()
        mask1, mask2 = color_segment(frame)
        final_frame = invisibility_effect(frame, mask1, mask2, backg)
        cv2.imshow("INVISIBLE CLOAK", final_frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
    vid_cap.release()
    cv2.destroyAllWindows()
####################################################################################################################

if __name__ == "__main__":
    main()