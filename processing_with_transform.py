from PIL import Image
from transform import RGBTransform
from trying_out_colors import get_main_color

image = Image.open("source.png")
image = image.convert('RGB')
data = get_main_color("destination.png")
# image.show()

red = RGBTransform().mix_with(data).applied_to(image)
red.show()
red.save("new_file.png")