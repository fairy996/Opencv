#梯度 = 膨胀 - 腐蚀
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\pie.png")
kernel = np.ones((7,7),np.uint8)
fs = cv2.erode(img,kernel,iterations=5)
pz = cv2.dilate(img,kernel,iterations=5)

#梯度运算
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
res = np.hstack((fs,pz,gradient))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()