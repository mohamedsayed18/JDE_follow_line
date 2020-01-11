import numpy as np
import cv2

image = cv2.imread(Russian_flag.svg) #load image

# define the lower and upper bound of our color in BGR
lower_red = np.array([0,60,255]) #lower limit
upper_red = np.array([40,0,255]) #upper limit
# this function return image with values of (0 or 1) for each pixel
# 0 if out of range, 255 if in the range
mask = cv2.inrange(image, upper_red, lower_red) # filter the red color only
# Apply bitwise and operation which will output only the filterd color
output = cv2.bitwise_and(image, image, mask = mask) 

# show the images
cv2.imshow(output)
cv2.waitKey(0)

# Color detection Tutorials 
#https://github.com/atduskgreg/opencv-processing-book/blob/master/book/filters/in_range.md
#https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

#TODO find centre
#https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
