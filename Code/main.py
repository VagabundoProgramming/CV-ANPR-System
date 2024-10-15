import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

from plate_detection import *
from isomorphism_func import *
from number_plate_template_matching import *
from display_results import *
from image_rotation import *

directory = "C:/Users/G733/Visual Studio Code/Visual&Learning/Challenge1/CV-ANPR-System/Images/Test/"
figures = "C:/Users/G733/Visual Studio Code/Visual&Learning/Challenge1/CV-ANPR-System/Images/Figures/"
spain_mark = "C:/Users/G733/Visual Studio Code/Visual&Learning/Challenge1/CV-ANPR-System/Images/SpainMark.jpg"
score = ANPR_score()
for angle in os.listdir(directory):
    for name in os.listdir(directory+angle+"/"):
        print(name)
        contours = find_relevant_contours(directory+angle+"/"+name)
        contours = find_extremes(contours)
        index, error = calculate_error(contours)
        img = cv2.imread(directory+angle+"/"+name)


        #cv2.drawContours(img, contours[index], -1, (0,0,255), 100)
        pts = np.array([contours[index][0][0][0], contours[index][1][0][0], contours[index][2][0][0], contours[index][3][0][0]])
        img = four_point_transform(img, pts, custom_resolution=(520, 110))
        prediction = template_matching(img, figures, spain_mark=spain_mark)

        score.add_guess(name, prediction, angle)

        if False:
            print(prediction)
            cv2.imshow(name, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

plot_result_distr_by_angle(score)
plot_results_distr(score)
char_confusion_matrix_by_angle(score)
char_confusion_matrix_full(score)
print(model_char_acc(score))
print(threshold_acc(score, 7))
