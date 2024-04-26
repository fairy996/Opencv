"""
- 1)使用高斯滤波器，以平滑图像，滤除噪声。
- 2)计算图像中每个像素点的梯度强度和方向。
- 3)应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。----->极大值抑制
- 4)应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。
- 5)通过抑制孤立的弱边缘最终完成边缘检测。
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\lena.jpg",cv2.MORPH_GRADIENT)
value1 = cv2.Canny(img,120,250)
value2 = cv2.Canny(img,50,100)

res = np.hstack((value1,value2))
cv_show('res',res)