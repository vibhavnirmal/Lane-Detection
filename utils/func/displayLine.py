import cv2
import numpy as np
import warnings
from utils.func.addText import addText

class displayLine(object):
    """docstring for display."""

    def __init__(self):
        super(displayLine, self).__init__()

    def display(image, lines):
        line_image = np.zeros_like(image)
        try:
            if lines is not None:
                for x1, y1, x2, y2 in lines:
                    try:
                        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    except OverflowError:
                        print("Overflowerror")
                        textOnVideo = addText.add_text(10, 50, "No Line to show", image, 5, 1, 0, 155, 255, 255, 1)
                        return textOnVideo
            return line_image
        except TypeError:
            print("TypeError")
            textOnVideo = addText.add_text(10, 50, "No Line to show", image, 5, 1, 0, 155, 255, 255, 1)
            return textOnVideo
