import numpy as np
import warnings
from utils.func.addText import addText

class coords(object):
    """docstring for make_coordinates."""

    def __init__(self):
        super(make_coordinates, self).__init__()

    def make_coordinates(img, line_para):
        slope, intercept = line_para
        try:
            y1 = img.shape[0]
            y2 = int(y1*(3.6/5))
            x1 = int((y1 - intercept)/slope)
            x2 = int((y2 - intercept)/slope)

            return np.array([x1, y1, x2, y2])
        except OverflowError:
            print("OverflowError")
            # textOnVideo = addText.add_text(0, 0, "txt is here", img)
            # return textOnVideo
