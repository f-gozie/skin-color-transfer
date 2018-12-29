from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
# from PIL import Image
from trying_out_colors import get_main_color

# Find the dominant color of the image
source_image = get_main_color("source.png")
destination_image = get_main_color("destination.png")

# Unpack the tuple containing the dominant color
a, b, c = source_image
d, e, f = destination_image

# Ensure it is an RGB color before converting to Lab Color Space
# Source
source_rgb = sRGBColor(a, b, c)
source_lab = convert_color(source_rgb, LabColor)
# Destination
destination_rgb = sRGBColor(d, e ,f)
destination_lab = convert_color(destination_rgb, LabColor)

# Then find the color difference and print it to the console
difference = delta_e_cie2000(source_lab, destination_lab)
print(difference)