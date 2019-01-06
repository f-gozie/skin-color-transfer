import numpy
from PIL import Image
from trying_out_colors import get_main_color
from color_difference import find_color_difference_with_tuple
import time

start = time.time()
source_image = "source.png"
destination_image = "drill.png"


value = get_main_color(source_image)
destant = get_main_color(destination_image)
color_diff = find_color_difference_with_tuple(value, destant)
# test = 

destination = Image.open(destination_image)
new = Image.new("RGB", destination.size, 0xffffff)
width, height = destination.size
for x in range(width):
	for y in range(height):
		destiny = destination.getpixel((x, y))
		# total_diff = tuple([int(x) for x in total_diff])
		# final = tuple([ a+color_diff for a in destiny])
		final = tuple(numpy.add(color_diff, destiny))
		final = [int(x) for x in final]
		final = tuple([ x-100 for x in final])
		# print(final)
		new.putpixel((x, y), final)


new.save("good.png")
end = time.time()

print(end-start)