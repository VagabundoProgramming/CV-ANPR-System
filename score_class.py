# This file contains a class to store the accuracity of our model

# Libraries
import numpy as np


class ANPR_score():
	def __init__(self):
		self.guesses = 0
		self.correct_guesses = 0
		self.guesses_distr = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
		self.confusion_matrix = np.zeros((30, 30), dtype = int)
		self.val2idx = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "B":10, "C":11, "D":12, "F":13, "G":14, "H":15, "J":16, "K":17, "L":18, "M":19, "N":20, "P":21, "R":22, "S":23, "T":24, "V":25, "W":26, "X":27, "Y":28, "Z":29}

	def return_guesses(self):
		return(self.guesses)
	
	def reset(self):
		self.guesses = 0
		self.correct_guesses = 0
		self.confusion_matrix = np.zeros((30, 30), dtype = int)
		self.guesses_distr = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

	def char_accuracity(self):
		if self.guesses == 0:
			return -1
		
		total_correct_chars = 0
		for x in self.confusion_matrix.size()[0]:
			total_correct_chars += self.matrix_val[x,x]
		
		return total_correct_chars / self.guesses

	def full_plate_acc(self):
		if self.guesses == 0:
			return -1
		return self.correct_guesses / self.guesses

	def guess_distr(self):
		return self.guesses_distr

	def char_confusion_matrix(self):
		return self.confusion_matrix

	def add_guess(self, gt, pred):
		if len(gt) != 7:
			return -1
		if len(pred) != 7:
			return -1

		self.guesses += 1

		c = 0
		for x in range(0, 7, 1):
			if gt[x] == pred[x]:
				c+= 1
				
		self.guesses_distr[c] += 1
		
		if gt == pred:
			self.correct_guesses += 1		

		for x in range (0, 7, 1):

			self.confusion_matrix[self.val2idx[gt[x]]] [self.val2idx[pred[x]]] += 1




a = ANPR_score()
a.add_guess("0123BCD", "0124BBB")
#print(a.guesses_distr)
print(a.char_confusion_matrix())


print("juan")

				
