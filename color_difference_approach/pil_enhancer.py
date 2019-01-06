from PIL import Image, ImageEnhance

im = Image.open("final.png")
enhancer = ImageEnhance.Contrast(im)
enhanced_im = enhancer.enhance(79)

enhancer = ImageEnhance.Brightness(im)
enhanced_im = enhancer.enhance(0.103)

enhanced_im.save("enhanced_sample_bright.png")