#Sobel因子

# 从右到左，从下到上来进行计算
#出现负数，因此要取绝对值，保证所有边界可以正确的呈现出来
#不建议直接将左右和上下的求取都设置为1，因为那样会出现重影且部分边界不会被呈现出来


import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\lena.jpg",cv2.IMREAD_GRAYSCALE)

dst=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
dst = cv2.convertScaleAbs(dst)
dst2=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
dst2 = cv2.convertScaleAbs(dst2)
dst3=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
dst3 = cv2.convertScaleAbs(dst3)
res = cv2.addWeighted(dst,0.5,dst2,0.5,0)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()