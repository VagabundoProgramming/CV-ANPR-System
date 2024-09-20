## This code is based of
# https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/


# import libraries
import numpy as np
import cv2
import argparse

# Ordered points function. Given 4 coordinates on an image it will
# return a list of them ordered. It is crucial to order the points.
def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	ordered_pts = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	ordered_pts[0] = pts[np.argmin(s)]
	ordered_pts[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	ordered_pts[1] = pts[np.argmin(diff)]
	ordered_pts[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return ordered_pts

def four_point_transform(image, pts, custom_resolution = False):
	# obtain a consistent order of the points and unpack them
	# individually
	ordered_pts = order_points(pts)
	(tl, tr, br, bl) = ordered_pts
	
    # We may like to have consistent sizes for the future, consider modifying
	if not custom_resolution:
		print("a")

		# compute the width of the new image, which will be the
		# maximum distance between bottom-right and bottom-left
		# x-coordiates or the top-right and top-left x-coordinates
		widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
		widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
		maxWidth = max(int(widthA), int(widthB))
		# compute the height of the new image, which will be the
		# maximum distance between the top-right and bottom-right
		# y-coordinates or the top-left and bottom-left y-coordinates
		heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
		heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
		maxHeight = max(int(heightA), int(heightB))
		# now that we have the dimensions of the new image, construct
		# the set of destination points to obtain a "birds eye view",
		# (i.e. top-down view) of the image, again specifying points
		# in the top-left, top-right, bottom-right, and bottom-left
		# order
		
	# If we want standarized images we may get away with simply selecting our own values for this space

		result_coord = np.array([
								[0, 0],
								[maxWidth - 1, 0],
								[maxWidth - 1, maxHeight - 1],
								[0, maxHeight - 1]], dtype = "float32")
	
	else: 
		print(custom_resolution)
		print(custom_resolution[0])
		result_coord = np.array([
								[0,0],
								[custom_resolution[0], 0]
								[custom_resolution[0],custom_resolution[1]],
								[0,custom_resolution[1]]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(ordered_pts, result_coord)
	warped_image = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	# return the warped image
	return warped_image



# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them

#TEST basically

image = cv2.imread('C:/Users/Daniel Gil/Documents/Visual Piss Code/CV ANPR/Test\Frontal/3340JMF.jpg', 0)

pts = np.array(([[0, 0], [0, 1000], [1000, 00], [500, 1000]]), dtype = "float32")
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts, custom_resolution=False) # [520, 110]
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
