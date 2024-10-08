# This file contains a class to store the accuracity of our model

# Libraries
import numpy as np


class ANPR_score():
	def __init__(self):
		self.np_guess_distr = {}#{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0} # Number plate guess distribution
		self.np_char_confusion_matrix = {}#np.zeros((30, 30), dtype = int)     # Number plate char_confusion_matrix
		self.val2idx = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "B":10, "C":11, "D":12, "F":13, "G":14, "H":15, "J":16, "K":17, "L":18, "M":19, "N":20, "P":21, "R":22, "S":23, "T":24, "V":25, "W":26, "X":27, "Y":28, "Z":29}


	# Reset the values of the guesses_distribution and confusion_matrix
	def clear(self):
		self.np_guess_distr = {} #{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
		self.np_char_confusion_matrix = {} #np.zeros((30, 30), dtype = int)
		

	# Returns the number of guesses on a specific angle or all of them
	def guesses(self, angle = None):
		guesses = 0
		if self.np_guess_distr == {}:
			return guesses

		if angle == None: # Return the total number of guesses made
			guesses = sum([sum(list(value.values())) for value in [dicts for dicts in self.np_guess_distr.values()]])
			return guesses
		
		if angle not in self.np_guess_distr.keys(): # Angle not in the dict
			return -1
		
		else: # Return the total amount of guesses made in a specific angle
			guesses = sum([value for value in self.np_guess_distr[angle].values()])
			return guesses


	# Returns the accuracy of the algorithm across all angles
	def char_accuracity(self, angle = None):
		guesses = 0
		if self.np_char_confusion_matrix == {}: #No guesses have been made
			return guesses

		if angle == None: # Return the char_accuracity for all angles 
			char_guesses = self.guesses() * 7
			correct_guesses = sum([sum(np.diag(matrix)) for matrix in self.np_char_confusion_matrix.values()])
			return correct_guesses / char_guesses

		if angle not in self.np_char_confusion_matrix.keys(): # Angle not in the dict
			return -1
		
		else: # Return the accuracy of a specific angle:
			char_guesses = self.guesses(angle) * 7
			correct_guesses = sum(np.diag(self.np_char_confusion_matrix[angle]))
			return correct_guesses / char_guesses

	# Return the accuracy of getting at least n characters of the number plate correctly
	# By default all the angles, can be specified if desired
	def plate_acc(self, n = 7, angle = None):
		acc = 0
		if self.np_guess_distr == {}: # No guesses made
			return acc
		
		if angle == None: # Guesses from all angles
			total_guesses = self.guesses()
			correct_guesses = 0
			for key in self.np_guess_distr.keys():
				for x in range (n, 8, 1):
					correct_guesses += self.np_guess_distr[key][x]
			return correct_guesses / total_guesses

		if angle not in self.np_guess_distr.keys(): # Angle not in the current scope
			return -1

		else: 
			total_guesses = self.guesses(angle)
			correct_guesses = 0
			for x in range (n, 8, 1):
				correct_guesses += self.np_guess_distr[angle][x]
			return correct_guesses / total_guesses
		

	# Return the specified part of the guess_distr
	def guess_distr(self, angle = None):
		if angle == None: # Return whole char_confusion_matrix
			return self.np_guess_distr
		if angle not in self.np_guess_distr.keys(): # Angle not in the current scope
			return -1
		else:
			return self.np_guess_distr[angle]

	# Returns the specified part of the char_confusion_matrix
	def char_confusion_matrix(self, angle = None):
		if angle == None: # Return whole char_confusion_matrix
			return self.np_char_confusion_matrix
		if angle not in self.np_char_confusion_matrix.keys(): # Angle not in the current scope
			return -1
		else:
			return self.np_char_confusion_matrix[angle]

	def add_guess(self, gt, pred, angle):
		if len(gt) != 7 or len(pred) != 7: # Ensure inputs are correct
			return -1

		if angle not in self.np_guess_distr.keys():
			self.np_guess_distr[angle] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
			self.np_char_confusion_matrix[angle] = np.zeros((30, 30), dtype = int)

		# Update np_guess_distr
		correct_chars = 0
		for x in range(0, 7, 1):
			if gt[x] == pred[x]:
				correct_chars += 1
				
		self.np_guess_distr[angle][correct_chars] += 1
			
		# Update np_char_confusion_matrix
		for x in range (0, 7, 1):
			self.np_char_confusion_matrix[angle][self.val2idx[gt[x]]] [self.val2idx[pred[x]]] += 1
