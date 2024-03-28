import cv2
import numpy as np
from matplotlib import pyplot as plt

#显示图像函数
def cv_show(image,img):
    cv2.imshow(image,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#读取图像
img = cv2.imread('F:/Deep Learning/Opencv_Study/material/lena.jpg',0)
plt.subplot(121)
plt.hist(img.ravel(),256)
cv_show('img',img)
equ = cv2.equalizeHist(img)
cv_show('equ',equ)
plt.subplot(121)
plt.hist(img.ravel(),256)
plt.subplot(122)
plt.hist(equ.ravel(),256)
plt.show()


