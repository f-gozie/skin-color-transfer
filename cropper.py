from PIL import Image

def crop(image, coords, saved_location):
	# image_obj = Image.open(path)
	cropped_image = image.crop(coords)
	cropped_image.save(saved_location)

image = Image.open("source.png")
crop(image, (400, 400, 706, 1050), "cropped.png")