import cv2


class TextOnScreen:
    """docstring for addText."""

    def __init__(self):
        super(TextOnScreen, self).__init__()
        self.fontNum = [["FONT_HERSHEY_SIMPLEX", 0],
                        ["FONT_HERSHEY_PLAIN", 1],
                        ["FONT_HERSHEY_DUPLEX", 2],
                        ["FONT_HERSHEY_COMPLEX", 3],
                        ["FONT_HERSHEY_TRIPLEX", 4],
                        ["FONT_HERSHEY_COMPLEX_SMALL", 5],
                        ["FONT_HERSHEY_SCRIPT_SIMPLEX", 6],
                        ["FONT_HERSHEY_SCRIPT_COMPLEX", 7],
                        ["FONT_ITALIC", 16]
                        ]

    def add_text(self, x, y, textOnScreen, image, fontNumber, fontSize, r, g,
                 b, op, stroke):
        position = (x, y)
        return cv2.putText(image, textOnScreen, position,
                           self.fontNum[fontNumber][1], fontSize,
                           (r, g, b, op), stroke)
