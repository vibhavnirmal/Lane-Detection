import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings
from utils.func.canny import canny
from utils.func.lineImg import lineImg
from utils.func.makeCoords import coords
from utils.func.displayLine import displayLine
from utils.func.roi import roi

class fromImage(object):
    """docstring for fromImage."""

    def __init__(self):
        super(fromImage, self).__init__()

    def image():
        img = cv2.imread("data/image/dcam2.jpg")
        lane_image = np.copy(img)
        canny_img = canny.canny_det(lane_image)
        cropped_img = roi.roi(canny_img)
        lines = cv2.HoughLinesP(cropped_img, rho=1, theta=np.pi/180, threshold=50, lines=np.array([]), minLineLength=40, maxLineGap=3)
        avg_lines = lineImg.avg_line_img(lane_image, lines)
        line_image = displayLine.display(lane_image, avg_lines)
        combo = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

        plt.imshow(combo)

        cv2.imshow("image", combo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
