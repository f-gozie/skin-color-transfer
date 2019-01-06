from PIL import Image
from transform import RGBTransform
from trying_out_colors import get_main_color
from cropper import crop
from color_difference import find_color_difference

# Load the source and destination image
source = "source.png"
destination = "destination.png"
source_image = Image.open(source)
destination_image= Image.open(destination)

# Using provided coordinates, crop the image and save as cropped.png
coordinates = (400, 400, 706, 1050)
crop(source_image, coordinates, "cropped.png")

# Load the cropped image and find dominant color in the image
cropped = Image.open("cropped.png")
cropped_data = get_main_color("cropped.png")

# Find the Source - Destination Color Difference
difference = find_color_difference(source, destination)

red = RGBTransform().mix_with(cropped_data).applied_to(destination_image)
red.save("new_file.png")