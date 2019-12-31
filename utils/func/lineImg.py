import warnings
import numpy as np
from utils.func.addText import addText
from utils.func.makeCoords import coords

class lineImg(object):
    def __init__(self):
        super(lineImg, self).__init__()

    def avg_line_img(image, lines):
        left_ln, right_ln, left_fit, right_fit = [], [], [], []

        try:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)

                para = np.polyfit((x1, x2), (y1, y2), 1)

                if abs(para[0]) > 0.0002:
                    print(para[0])

                    slope = para[0]
                    intercept = para[1]

                    if slope < 0:
                        left_fit.append((slope, intercept))
                    else:
                        right_fit.append((slope, intercept))

            left_fit_avg = np.average(left_fit, axis = 0)
            right_fit_avg = np.average(right_fit, axis = 0)

            left_ln.append(left_fit_avg)

            if str(type(right_fit_avg)) == "<class 'numpy.float64'>":
                try:
                    right_ln.insert(len(right_ln), right_ln[-1])
                except IndexError:
                    print("IndexError")
            else:
                right_ln.append(right_fit_avg)
#         print(right_ln)

            # if str(type(right_fit_avg)) == "<class 'numpy.float64'>":
            #     right_fit_avg = right_ln[-1]
            # else:
            #     pass
#             print("yesssssss",right_fit_avg)

            left_line = coords.make_coordinates(image, left_fit_avg)
            right_line = coords.make_coordinates(image, right_fit_avg)

            return np.array([left_line, right_line])

        except TypeError:
            print("typeError")
            textOnVideo = addText.add_text(10, 50, "Keep Hands on Steering Wheel", image, 5, 1, 255, 0, 0, 255, 1)
            textOnVideo = addText.add_text(10, 80, "Lane Detection Failed", image, 5, 1, 255, 0, 0, 255, 1)
            return textOnVideo
