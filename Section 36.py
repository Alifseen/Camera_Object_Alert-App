import cv2
import numpy

## Loading an Image
image1 = cv2.imread("files/image.png")
print(image1.shape)
print(image1)

## Creating an Image
a = numpy.array([[[255, 0, 0],
  [255, 255, 255],
  [255, 255, 255],
  [187, 41, 160]],

 [[255, 255, 255],
  [255, 255, 255],
  [255,  255,  255],
  [255, 255, 255]],

 [[255, 255, 255],
  [0, 0, 0],
  [47, 255, 173],
  [255, 255, 255]]])

image2 = cv2.imwrite("files/image2.png", a)
