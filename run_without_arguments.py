from color_transfer import color_transfer
import numpy as np
import cv2
from cropper import crop
from temp_adjust import convert_temp
from PIL import Image

# Collect input from user, crop the source, then load the required images
source = input("Enter source image: ").lower()
source = crop(source)
source_image = cv2.imread(source)

destination = input("Enter destination image: ").lower()
destination_image = cv2.imread(destination)

transfer = color_transfer(source_image, destination_image)
cv2.imwrite("transfer.png", transfer)

converted_img = Image.open("transfer.png")
convert_temp(converted_img, 5000)