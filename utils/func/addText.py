import cv2
import numpy as np

global num
num = [["FONT_HERSHEY_SIMPLEX",0],
        ["FONT_HERSHEY_PLAIN",1],
        ["FONT_HERSHEY_DUPLEX",2],
        ["FONT_HERSHEY_COMPLEX",3],
        ["FONT_HERSHEY_TRIPLEX",4],
        ["FONT_HERSHEY_COMPLEX_SMALL",5],
        ["FONT_HERSHEY_SCRIPT_SIMPLEX",6],
        ["FONT_HERSHEY_SCRIPT_COMPLEX",7],
        ["FONT_ITALIC",16]
    ]

class addText(object):
    """docstring for addText."""

    def __init__(self):
        super(addText, self).__init__()


    def add_text(x, y, textOnScreen, image, fontNum, fontSize, r, g, b, op, stroke):
        position = (x, y)
        cv2.putText(image, textOnScreen, position, num[fontNum][1], fontSize, (r, g, b, op),stroke)
