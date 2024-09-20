import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

from plate_detection import *

directory = "Images/Test/Front/"
for name in os.listdir(directory):
    contours = find_relevant_contours(directory+name)
    contours = find_extremes(contours)
    index, error = calculate_error(contours)
    print(error, len(contours))
    img = cv2.imread(directory+name)
    cv2.drawContours(img, contours[index], -1, (0,0,255), 100)
    img = cv2.resize(img, (960, 540))
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
