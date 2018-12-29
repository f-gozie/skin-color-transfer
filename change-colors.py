# This script changes all specific colors in an image to a specific given color

import numpy as np
import cv2

im = cv2.imread('destination.png')
im[np.where((im == [103, 65, 46]).all(axis=2))] = [155, 99, 72]
cv2.imwrite('test.png', im)