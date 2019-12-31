import numpy as np
import cv2

class roi(object):
    """docstring for roi."""

    def __init__(self):
        super(roi, self).__init__()

    def roi(image):
        height = image.shape[0]
        width = image.shape[1]
#       print(width)
        poly = np.array([
            [(100, height), (width, height), (530, 350)]
        ])
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, poly, 255)
        masked_img = cv2.bitwise_and(image, mask)
        return masked_img
