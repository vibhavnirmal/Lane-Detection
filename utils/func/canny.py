import cv2

class canny(object):
    """docstring for canny."""

    def __init__(self):
        super(canny, self).__init__()

    def canny_det(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blur, 30, 110)
        return canny
