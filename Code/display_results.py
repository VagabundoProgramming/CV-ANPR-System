# This file will have functions that will help
# display the results of the ANPR system

# Esto probablemente no funciona debido a que no tengo actualmente e codigo adecuado de Score

import matplotlib.pyplot as plt
import numpy as np
#from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import SVC
from ANPR_Score_class import ANPR_score


# Displays a bar plot of the numbers of characters corectly guessed by angle.
def plot_result_distr_by_angle(score :ANPR_score):
    guess_distr = score.guess_distr()
    num_plots = len(guess_distr)
    ylabel_max = max([guess_distr[key][sub_key] for key in guess_distr.keys() for sub_key in guess_distr[key].keys()]) + 6

    fig, axs = plt.subplots(ncols = num_plots)
    fig.set_size_inches(18.5, 10.5)
    fig.suptitle('Guess Distribution by Angle\n ', fontsize=20)
    plt.setp(axs, xlim = (-1, 8), ylim = (0, ylabel_max))
    
    # Create Graph
    for n, key in enumerate(guess_distr.keys()):
        x = [str(key) for key in guess_distr[key].keys()]
        y = [n for n in guess_distr[key].values()]
    
        axs[n].title.set_text(str(key) + " angle")
        axs[n].set_ylabel('Number of images')
        axs[n].set_xlabel('Number of correctly guessed characters')
        
        axs[n].bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        axs[n].set_yticks(range(0, ylabel_max, 5))

    fig.tight_layout()
    #fig.savefig("Guess_by_angle")
    plt.show()


# Plot guess distribution, all angles together
def plot_results_distr(score: ANPR_score):
    guess_distr = score.guess_distr()
    x = [str(key) for key in list(guess_distr.values())[0].keys()]
    
    temp_dict = {}
    for sub_dict in guess_distr.values():
        for key, value in sub_dict.items():
            if key not in temp_dict.keys():
                temp_dict[key] = 0
            temp_dict[key] += value
    
    ylabel_max = max(temp_dict.values())+5

    fig, ax = plt.subplots()
    fig.set_size_inches(6.5, 10.5)
    fig.suptitle('Guess Distribution by Angle\n ', fontsize=20)
    ax.set_ylabel('Number of images')
    ax.set_xlabel('Number of correctly guessed characters')
    plt.setp(ax, xlim = (-1, 8), ylim = (0, ylabel_max))
    ax.set_yticks(range(0, ylabel_max, 5))
    
    weight_counts = {}
    for key, sub_dict in guess_distr.items():
        weight_counts[key] = list(sub_dict.values())

    bottom = np.zeros( len(list(list(guess_distr.values())[0].keys())))
    
    # Add values to the graph
    for angle, weight in weight_counts.items():
        #ax.bar(x, weight, 0.2 , label = angle) #,bottom = bottom)
        ax.bar(x, weight, 0.2 , label = angle, bottom = bottom)
        bottom += weight

    ax.legend(loc="upper right")

    fig.tight_layout()
    #fig.savefig("Guess_by_all_angles")
    plt.show()
    return


# Plots the confusion matrices for each angle
def char_confusion_matrix_by_angle(score: ANPR_score):
    score_confusion_matrix = score.char_confusion_matrix()

    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    for key in score_confusion_matrix.keys():
        fig, ax = plt.subplots(ncols = 1, figsize = (12, 12))

        data = np.array(score_confusion_matrix[key])
        disp = ConfusionMatrixDisplay(data, display_labels = labels)
        
        disp.plot(ax=ax)
        disp.ax_.set_title(key + " angle", fontdict = {"fontsize" : 25}, pad = 5)

        #fig.savefig("Char_conf_matrix_by_angle "+key)
        plt.show()
    return


# Plots a confusion matrix for all values
def char_confusion_matrix_full(score: ANPR_score):
    score_confusion_matrix = score.char_confusion_matrix()

    full_conf = np.zeros((30, 30), dtype=int)
    for value in score_confusion_matrix.values():
        full_conf += np.array(value)

    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    fig, ax = plt.subplots(ncols = 1, figsize = (12, 12))

    
    disp = ConfusionMatrixDisplay(full_conf, display_labels = labels)
        
    disp.plot(ax=ax)
    disp.ax_.set_title("Confusion Matrix of the Model", fontdict = {"fontsize" : 25}, pad = 1)

    #fig.savefig("Char_conf_matrix_by_angle "+key)
    plt.show()
    return

def model_char_acc(score:ANPR_score):
    message = "The model character accuracy is of:\n"
    message += str(score.char_accuracity()) + "\n\n"
    message += "For specific angles the accuracy is of:"
    for angle in score.guess_distr().keys():
        message += "\n" + str(angle) + ": " +  str(score.char_accuracity(angle)) 

    return(message)

def threshold_acc(score:ANPR_score, n = 7):
    message = "The models accuracy of at least " + str(n) + " characters is of:\n"
    message += str(score.plate_acc(n)) + "\n\n"
    message += "For specific angles the accuracy of at least " +str(n) + " characters is of:"
    for angle in score.guess_distr().keys():
        message += "\n" + str(angle) + ": " +  str(score.plate_acc(n, angle)) 

    return(message)



### TEST CODE ###
"""
a = ANPR_score()

a.add_guess("555555D", "1234BCD", "above")
a.add_guess("5555555", "1235BCD", "above")
a.add_guess("1234BCD", "1235BCD", "above")
for x in range (0, 100, 1):
    a.add_guess("1234BCD", "1234BCD", "above")
a.add_guess("1234BCD", "BBBBBBB", "b")

"""
#plot_result_distr_by_angle(a)
#plot_results_distr(a)
#char_confusion_matrix_by_angle(a)
#char_confusion_matrix_full(a)
#print(model_char_acc(a))
#print(threshold_acc(a, 7))
