#%% md
### 礼帽与黑帽
# - 礼帽 = 原始输入-开运算结果
# - 黑帽 = 闭运算-原始输入

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("F:\Deep Learning\Opencv_Study\material\dige.png")
kernel = np.ones((7,7),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat  = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT, kernel)
res = np.hstack((tophat,blackhat))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()