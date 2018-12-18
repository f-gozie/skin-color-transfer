from PIL import Image
im = Image.open("arch.png")
# im.rotate(45).show()
x = im.histogram()
print(len(x))

max = 0
for a in x:
	if a > max:
		max = a

print(max)