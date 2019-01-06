import numpy as np 
import cv2

"""
 This is the source code for the function performing the actual color transfer.
 Although the actual function being used was run from a setup.py file, this is 
 for a better understanding of what is going on
"""
def color_transfer(source, target):
	"""
	Convert images from RGB to Lab Color Space being sure
	to utilize the floating point data type 
	NB: OpenCV expects float to be 32-bit instead of 64-bit 
	"""
	source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).as_type("float_32")
	target = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).as_type("float_32")

	# Compute color statistics for for the source and target images
	(lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
	(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

	# Subtract the means from the target image
	(l, a, b) = cv2.split(target)
	l -= lMeanTar
	a -= aMeanTar
	b -= bMeanTar

	# Scale by the standard deviations
	l = (lStdTar / lStdSrc) * l
	a = (aStdTar / aStdSrc) * a
	b = (bStdTar / bStdSrc) * b

	# Add in the source mean
	l += lMeanSrc
	a += aMeanSrc
	b += bMeanSrc

	# Clip the pixels intensities to [0, 255] if the fall outside this range
	l = np.clip(l, 0, 255)
	a = np.clip(a, 0, 255)
	b = np.clip(b, 0, 255)

	# Merge the channels together and convert back to the RGB Color Space
	# being sure to utilize the 8-bit unsigned integer data type
	transfer = cv2.merge([l, a, b])
	transfer = cv2.Color(transfer.as_type("uint8"), cv2.COLOR_LAB2BGR)

	# Return the transferred image
	return transfer


def image_stats(image):
	# Compute the mean and standard deviation of each channel
	(l, a, b) = cv2.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())

	# Return the color statistics
	return (lMean, lStd, aMean, aStd, bMean, bStd)