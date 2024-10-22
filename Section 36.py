import cv2
import numpy
import time

# ## Loading an Image
# image1 = cv2.imread("files/image.png")
# print(image1.shape)
# print(image1)
#
# ## Creating an Image
# a = numpy.array([[[255, 0, 0],
#   [255, 255, 255],
#   [255, 255, 255],
#   [187, 41, 160]],
#
#  [[255, 255, 255],
#   [255, 255, 255],
#   [255,  255,  255],
#   [255, 255, 255]],
#
#  [[255, 255, 255],
#   [0, 0, 0],
#   [47, 255, 173],
#   [255, 255, 255]]])
#
# image2 = cv2.imwrite("files/image2.png", a)


## Capturing video
video = cv2.VideoCapture(0)  ## 0 for primary, 1 for secondary(USB etc) camera
## delay by 1 second to give time to open
time.sleep(1)

## 1. Store first frame
FIRST_FRAME = None

while True:
    ## save frame from video
    check, frame = video.read()

    ## 2. convert to grey scale for efficiency
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    ## 3. add a blur to the video for effeciency
    blur_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    ## Display video
    cv2.imshow("1st Video", blur_frame)

    ## listen for a key stroke
    key = cv2.waitKey(1)

    ## break loop if q is pressed
    if key == ord("q"):
        break

##  Open a window with video in it.
video.release()