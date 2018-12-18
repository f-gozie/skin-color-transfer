# This script changes all specific colors in an image to a specific given color

import numpy as np
import cv2

im = cv2.imread('arch.png')
im[np.where((im == [0, 0, 0]).all(axis=2))] = [0, 33, 166]
cv2.write('test.png', im)