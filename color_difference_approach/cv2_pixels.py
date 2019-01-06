import cv2
import numpy as np
import time
from trying_out_colors import get_main_color
from PIL import Image
from color_difference import find_color_difference_with_tuple

start = time.time()
m = cv2.imread("destination.png")
dest_shape = m.shape
x, y, z = dest_shape
tup = (x, y)


im = Image.new('RGB', tup)
source = get_main_color("source.png")

def solve():
	m = cv2.imread("destination.png")
	lis = []
	h, w, bpp = np.shape(m)
	for py in range(0, h):
		for px in range(0, w):
			destination = tuple(m[py][px])
			difference = find_color_difference_with_tuple(source, destination)
			# added = tuple(np.add(difference, source))
			added = tuple([ a+difference for a in destination])
			added = tuple([int(x) for x in added])
			lis.append(added)
	return lis
# print(solve("destination.png"))
x = solve()
im.putdata(x)
im.save("fact.png")
end = time.time()
print(end-start)

# solve("destination.png")

# im = Image.new('RGB', tup)
# im.putdata([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

# Get image properties
# h, w, bpp = np.shape(m)
# source = get_main_color("source.png")

# for py in range(0, h):
# 	for px in range(0, w):
# 		x = tuple(m[py][px])
# 		diff = find_color_difference_with_tuple(source, x)
# 		# added = tuple(np.add(diff, source))
# 		added = tuple([ a+diff for a in x])
# 		added = tuple([int(a) for a in added])
# 		print(added)

# # im.save("whole.png")



# end = time.time()
# tot = end-start
# print(tot)
