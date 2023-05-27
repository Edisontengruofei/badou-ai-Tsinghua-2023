import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("test.jpg", 1)
cv2.imshow("src", img)

(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

result = cv2.merge((bH, gH, rH))
cv2.imshow("dst_rgb", result)
cv2.waitKey()