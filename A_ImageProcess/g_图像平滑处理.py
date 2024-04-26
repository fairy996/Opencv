import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\lenaNoise.png")
plt.subplot(2,1,1)
plt.imshow(img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#均值滤波
blur = cv2.blur(img,(3,3))
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.subplot(2,1,2)
plt.imshow(blur)
plt.show()
#方框滤波
box = cv2.boxFilter(img,-1,(3,3),normalize=False)#normalize为False表示不进行归一化操作，如果产生越界情况，则取最大值255，若narmalize为True表示进行归一化操作，此时方框滤波与均值滤波效果相同
#高斯滤波
aussian = cv2.GaussianBlur(img,(5,5),1)
#中值滤波
median = cv2.medianBlur(img,5)

res = np.hstack((blur,aussian,median))
