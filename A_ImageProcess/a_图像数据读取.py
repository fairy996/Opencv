import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('F:\Deep Learning\Opencv_Study\material\cat.jpg')
img2 = cv2.imread('F:\Deep Learning\Opencv_Study\material\dog.jpg',cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image',img)
# cv2.waitKey(0)

#显示图像函数
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv_show('image',img)
cv_show('image',img2)
#图像保存
#cv2.imwrite('路径'，图像变量名)

#视频

