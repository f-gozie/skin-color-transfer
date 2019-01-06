from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from trying_out_colors import get_main_color


def find_color_difference_with_tuple(tuple_1, tuple_2):
	a, b, c = tuple_1
	d, e, f = tuple_2

	rgb_1 = sRGBColor(a, b, c)
	lab_1 = convert_color(rgb_1, LabColor)
	rgb_2 = sRGBColor(d, e, f)
	lab_2 = convert_color(rgb_2, LabColor)

	difference = delta_e_cie2000(lab_1, lab_2)
	return difference

def find_color_difference_with_path(source_path, destination_path):
	# Find the dominant color of the image
	source_image = get_main_color(source_path)
	destination_image = get_main_color(destination_path)

	# Unpack the tuple containing the dominant color and place in individual variables
	a, b, c = source_image
	d, e, f = destination_image

	# Ensure it is an RGB color before converting to Lab Color Space
	source_rgb = sRGBColor(a, b, c)
	source_lab = convert_color(source_rgb, LabColor)
	destination_rgb = sRGBColor(d, e, f)
	destination_lab = convert_color(destination_rgb, LabColor)

	# Find the color difference 
	difference = delta_e_cie2000(source_lab, destination_lab)

	return difference