import numpy as np
import cv2
 
#读取图片
img = cv2.imread('Z_ClassTask/task3/image/target_Img.png')
#图像转换为灰度图像
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#灰度二值化
_,mask = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),100,255,cv2.THRESH_BINARY_INV)
#_,mask = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)
#mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#第一种方法 img:输入图像；mask为单通道二值图掩模，非零位置为需要修复的地方；3:领域大小，在修复
#开路中图像素的范围
#dst = cv2.inpaint(img,mask,10,cv2.INPAINT_TELEA)
#第二种方法 INPAINT_NS
#区域内的灰度值变化最小。
dst = cv2.inpaint(img,mask,10,cv2.INPAINT_NS) #3:领域大小
cv2.imshow('img0',img)
#cv2.imshow('img10',mask1)
cv2.imshow('img1',mask)
cv2.imshow('img2',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()