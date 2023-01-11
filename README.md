# Invisibility Cloak 

This is a project for the *Introduction to Python* event by the **FreeScape IIIT Kalyani** club.

This is a very popular project, and I will be following some articles and/or github links, all of which we will provided as references for the reader to peruse.

We will be using OpenCV for this project. 

The idea behind the work is that we first capture the background image. Then we detect and segment the cloth(it is important that a **red** cloth is used, as the code has been written for that specific colour).


### Part I

After starting the camera, give the program some time to capture the background. This will be used to mask the cloak, which will provide the *invisibility* effect.

### Part II

Now we need to perform color segmentation. This is done by detecting where the red colour is present. Now we apply a mask, due to which only the red color parts are visible and everything else is black. It will look like this: 

### Part III

Now we need to remove the color segmented area and replace it with the background pixels which were stored since we ran a loop for code to store the background pixels. Now it looks like this: 


## References/Links

- [Invisible cloak using OpenCV](https://learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/)
- [Invisible cloak using OpenCV(GeeksForGeeks)](https://www.geeksforgeeks.org/invisible-cloak-using-opencv-python-project/)
- [Color segmentation](https://medium.com/srm-mic/color-segmentation-using-opencv-93efa7ac93e2)
- [OpenCV documentation](https://docs.opencv.org/master/index.html)


