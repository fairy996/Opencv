import cv2
import matplotlib.pyplot as plt
import numpy as np
#开运算：先腐蚀再膨胀
#闭运算，先膨胀再腐蚀
img = cv2.imread("F:\Deep Learning\Opencv_Study\material\dige.png")
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
res = np.hstack((opening,closing))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()