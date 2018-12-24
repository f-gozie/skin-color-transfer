from PIL import Image
from transform import RGBTransform
from trying_out_colors import get_main_color
from cropper import crop

# Load the source and destination image
source = Image.open("source.png")
destination = Image.open("destination.png")

# Using provided coordinates, crop the image and save as cropped.png
coordinates = (400, 400, 706, 1050)
crop(source, coordinates, "cropped.png")

# Load the cropped image and find dominant color in the image
cropped = Image.open("cropped.png")
cropped_data = get_main_color("cropped.png")

red = RGBTransform().mix_with(cropped_data).applied_to(destination)
red.save("new_file.png")