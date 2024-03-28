import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\dige.png")

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((3,3),np.uint8)#相当于定义卷积区间的大小，区间越大腐蚀效果就越强，区间越小就越弱，迭代次数越多服饰效果就越强，次数越少，腐蚀效果就越弱
erosion = cv2.erode(img,kernel,iterations=1)
erosion = cv2.dilate(erosion,kernel,iterations=1)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
img1 = cv2.imread("F:\Deep Learning\Opencv_Study\material\pie.png")
kernel = np.ones((30,30),np.uint8)
erosion1 = cv2.dilate(img1,kernel,iterations=1)
erosion2 = cv2.dilate(img1,kernel,iterations=2)
erosion3 = cv2.dilate(img1,kernel,iterations=5)

res = np.hstack((erosion1,erosion2,erosion3))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
