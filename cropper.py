from PIL import Image


def crop(image):
	"""
		This function just takes a variable containing the name of the
		image to be worked on, then using the fixed coordinates, crops
		the image so that there wouldn't be any excess black on the 
		image any more and returns the name of the cropped image
	"""
	image_obj = Image.open(image)
	# coords = (600, 600, 700, 1050)
	coords = (400, 400, 706, 1050)
	cropped = "cropped.png"
	cropped_image = image_obj.crop(coords)
	cropped_image.save(cropped)
	return cropped

# crop("img_2.jpg")