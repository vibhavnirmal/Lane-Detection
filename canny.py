import cv2


class canny:
    def __init__(self):
        pass

    def canny_det(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        theCanny = cv2.Canny(blur, 30, 110)
        return theCanny
