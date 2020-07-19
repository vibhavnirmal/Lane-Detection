# import warnings

import cv2
import numpy as np

from addText import TextOnScreen


class displayLine:
    def __init__(self):
        super(displayLine, self).__init__()
        self.showText = TextOnScreen()

    def display(self, image, lines):
        line_image = np.zeros_like(image)
        try:
            if lines is not None:
                try:
                    for x1, y1, x2, y2 in lines:
                        try:
                            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        except OverflowError:
                            print("Overflowerror")
                            textOnVideo = self.showText.add_text(
                                10, 50, "No Line to show", image, 5, 1, 0, 155,
                                255, 255, 1)
                            return textOnVideo
                except ValueError:
                    print("Value Error")
            return line_image
        except TypeError:
            print("TypeError")
            # textOnVideo = self.showText.add_text(
            #     10, 50, "No Line to show", image, 5, 1, 0, 155, 255, 255, 1)
            # return textOnVideo
