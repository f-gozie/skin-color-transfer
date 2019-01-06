from PIL import Image
import numpy as np
import cv2


# Get the dominant color from the image with the get_main_color() function
def get_main_color(file):
	img = Image.open(file)
	colors = img.getcolors(50000)
	max_occurence, most_present = 0, 0
	try:
		for c in colors:
			if c[0] > max_occurence:
				(max_occurence, most_present) = c
		return most_present
	except TypeError:
		raise Exception("Too many colors in the image")


# file_name = "cropped.png"
# image = Image.open(file_name)
# main_color = get_main_color(file_name)
# print(main_color)