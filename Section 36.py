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

    ## 4. Save the first frame in a variable so that other frames can be compared to it
    if FIRST_FRAME is None:
        FIRST_FRAME = blur_frame

    ## 5. Create a frame that only shows the difference between current frame and first frame
    diff_frame = cv2.absdiff(FIRST_FRAME, blur_frame)

    ## 6. Increase the whiteness of the frame
    threshold_frame = cv2.threshold(diff_frame, 60, 255, cv2.THRESH_BINARY)[1]

    ## 7. improve the difference frame
    dilated_frame = cv2.dilate(threshold_frame, None, iterations=2)

    ## 8. Store outline of new objects in frame
    contours, check = cv2.findContours(dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ## 9. Create rectangle around the new object oultine
    ## 10. iterate over each frame object outline
    for contour in contours:
        ## 11. if the new outline is not very strong, go to next line
        if cv2.contourArea(contour) < 5000:
            continue
        ## 12. if the new outline is strong, store its values and create a rectangle around it
        x, y, w, h = cv2.boundingRect(contour)
        ## we add the frame where it will be created, starting points, ending points, color, and number of colors (in case of BGR that is 3)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

    ## Display video
    cv2.imshow("1st Video", frame)

    ## listen for a key stroke
    key = cv2.waitKey(1)

    ## break loop if q is pressed
    if key == ord("q"):
        break

##  Open a window with video in it.
video.release()