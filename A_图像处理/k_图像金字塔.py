#高斯金字塔
#向下采样方法：越采样越小
#向上采样方法：越采样越大
#拉普拉斯金字塔:原图-down_up
import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\AM.png")

up = cv2.pyrUp(img)
cv_show('up',up)
down = cv2.pyrDown(up)
cv_show('down',down)

down1 = cv2.pyrDown(img)
down_up = cv2.pyrUp(down1)
res = img - down_up
cv_show('res',res)