import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

from plate_detection import *
from isomorphism_func import *
from number_plate_template_matching import *
from display_results import *
from image_rotation import *

directory = "Images/Test/Front/"
for name in os.listdir(directory):
    contours = find_relevant_contours(directory+name)
    contours = find_extremes(contours)
    index, error = calculate_error(contours)
    img = cv2.imread(directory+name)
    
    #cv2.drawContours(img, contours[index], -1, (0,0,255), 100)
    
    pts = order_points(contours[index])
    img = four_point_transform(img, pts, custom_resolution=(520, 110))

    print(template_matching(img, figures))
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
