import warnings

import cv2
# import matplotlib.pyplot as plt
import numpy as np

from canny import canny
from displayLine import displayLine
from lineImg import lineImg
# from makeCoords import coords
from roi import roi


class FromVideo:
    """docstring for FromVideo."""

    def __init__(self):
        super(FromVideo, self).__init__()
        self.theCanny = canny()
        self.showLine = displayLine()
        self.predLine = lineImg()
        self.theROI = roi()

    def video(self):
        cap = cv2.VideoCapture("data/video/HighWayRoad.mp4")

        while cap.isOpened():
            warnings.simplefilter('ignore', np.RankWarning)
            _, frame = cap.read()
            canny_img = self.theCanny.canny_det(frame)
            cropped_img = self.theROI.roi(canny_img)
            lines = cv2.HoughLinesP(cropped_img, rho=3, theta=np.pi/160,
                                    threshold=50, lines=np.array([]), 
                                    minLineLength=35, maxLineGap=6)
            avg_lines = self.predLine.avg_line_img(frame, lines)
            line_image = self.showLine.display(frame, avg_lines)
            combo = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
            cv2.imshow("image", combo)
            cv2.waitKey(1)


class FromImage:
    """docstring for FromImage."""

    def __init__(self):
        super(FromImage, self).__init__()
        self.theCanny = canny()
        self.showLine = displayLine()
        self.predLine = lineImg()
        self.theROI = roi()

    def image(self):
        img = cv2.imread("data/image/dcam2.jpg")
        lane_image = np.copy(img)
        canny_img = self.theCanny.canny_det(lane_image)
        cropped_img = self.theROI.roi(canny_img)
        lines = cv2.HoughLinesP(cropped_img, rho=1, theta=np.pi/180,
                                threshold=50, lines=np.array([]),
                                minLineLength=40, maxLineGap=3)
        avg_lines = self.predLine.avg_line_img(lane_image, lines)
        line_image = self.showLine.display(lane_image, avg_lines)
        combo = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

        # plt.imshow(combo)

        cv2.imshow("image", combo)
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow("image")


if __name__ == "__main__":
    vid = FromVideo()
    vid.video()
    # pic = FromImage()
    # pic.image()
