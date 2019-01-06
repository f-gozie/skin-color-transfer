import cv2
import numpy as np
import argparse


def level_color(file):
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', help="Path to input image.", default="final.png")
	args = parser.parse_args()

	image = cv2.imread(cv2.samples.findFile(args.input))
	if image is None:
		print('Could not open or find the image: ', args.input)
		exit(0)

	new_image = np.zeros(image.shape, image.dtype)

	alpha = 1.0    # Simple contrast control
	beta = 0       # Simple brightness control

	# Initialize the values
	print(" Basic Linear Transforms ")
	print("-------------------------")
	try:
		alpha = float(input("Enter the alpha value [1.0 - 3.0]: "))
		beta = int(input("Enter the beta value [0 - 100]: "))
	except ValueError:
		print("Error, not a number")


	"""
		Do the operation new_image(i, j) = alpha * image(i, j) + beta
		So as to show how pixels are accessed, I'll use for loops, 
		though this can be done alternatively by:
		new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
	"""

	for y in range(image.shape[0]):
		for x in range(image.shape[1]):
			for c in range(image.shape[2]):
				new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)

	# cv2.imshow("Original Image", image)
	# cv2.imshow("New Image", new_image)
	cv2.imwrite('new.png', new_image)

	cv2.waitKey()

level_color("final.png")