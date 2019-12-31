import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings
from utils.func.canny import canny
from utils.func.lineImg import lineImg
from utils.func.makeCoords import coords
from utils.func.displayLine import displayLine
from utils.func.roi import roi

class fromVideo(object):
    """docstring for video."""

    def __init__(self):
        super(fromVideo, self).__init__()

    def video():
        cap = cv2.VideoCapture("data/video/HighWayRoad.mp4")

        while cap.isOpened():
            warnings.simplefilter('ignore', np.RankWarning)
            _, frame = cap.read()
            canny_img = canny.canny_det(frame)
            cropped_img = roi.roi(canny_img)
            lines = cv2.HoughLinesP(cropped_img, rho=3, theta=np.pi/160, threshold=50, lines=np.array([]), minLineLength=35, maxLineGap = 6)
            avg_lines = lineImg.avg_line_img(frame, lines)
            line_image = displayLine.display(frame, avg_lines)
            combo = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
            cv2.imshow("image", combo)
            cv2.waitKey(1)
