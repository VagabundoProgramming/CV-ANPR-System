# This file code makes sure that the number plate detected is correctly rotated
# for its proper reading

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

def proper_rotation(image):
    img_h, img_w, __ = img.shape

    # Ensure the width is greater than the height
    if img_w < img_h:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        img_w, img_h = img_h, img_w

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    right_side = gray_image[0:img_h, img_w - img_w//10:img_w   ]
    right_side_mean = right_side.mean(axis=0).mean(axis=0)

    left_side =  gray_image[0:img_h, 0:img_w//10]
    left_side_mean = left_side.mean(axis=0).mean(axis=0)

    # If the side badge is not in the proper place
    if right_side_mean < left_side_mean:
        image = cv2.rotate(image, cv2.ROTATE_180)
        
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    upper_left_side = gray_image[0:img_h//2, 0:img_w//10]
    upper_left_side_mean = upper_left_side.mean(axis=0).mean(axis=0)

    lower_left_side = gray_image[img_h//2: img_h , 0:img_w//10]
    lower_left_side_mean = lower_left_side.mean(axis=0).mean(axis=0)

    # Make sure the lighter side of the side badge is in the lower part
    if upper_left_side_mean > lower_left_side_mean:
        image = cv2.flip(image, 0)

    #print(upper_left_side_mean)
    #print(lower_left_side_mean)

    #cv2.imshow("a", upper_left_side)
    #cv2.imshow("b", lower_left_side)
    return image


### MAIN CODE ###
img = cv2.imread("donkin i must.jpg")
img = cv2.imread("mockup.png")
img = cv2.imread("Code\mockup_flip.png")
img = cv2.imread("mockup_r.png")
height, width, channels = img.shape

img = proper_rotation(img)


cv2.imshow("Amongus", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.waitKey(0)
cv2.destroyAllWindows()
for x in range(0, 100, 1):
    cv2.imshow(str(x), img)
"""
