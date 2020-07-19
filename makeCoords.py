import numpy as np

# from addText import TextOnScreen


class coords:
    """docstring for make_coordinates."""

    def __init__(self):
        super(coords, self).__init__()
        # self.showText = TextOnScreen()
        self.prevX1 = 0
        self.prevY1 = 0
        self.prevX2 = 0
        self.prevY2 = 0

    def make_coordinates(self, img, line_para):
        slope, intercept = line_para
        try:
            y1 = img.shape[0]
            y2 = int(y1*(3.6/5))
            x1 = int((y1 - intercept)/slope)
            x2 = int((y2 - intercept)/slope)

            self.prevX1, self.prevX2, self.prevY1, self.prevY2 = x1, x2, y1, y2
            return np.array([x1, y1, x2, y2])
        except OverflowError:
            print("OverflowError")
            return np.array([self.prevX1, self.prevY1, self.prevX2,
                             self.prevY2])
            # textOnVideo = addText.add_text(0, 0, "txt is here", img)
            # return textOnVideo
