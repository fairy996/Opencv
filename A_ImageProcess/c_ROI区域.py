import cv2
import matplotlib.pyplot as plt
import numpy as np

cat = cv2.imread(r'F:\Deep Learning\Opencv_Study\material\cat.jpg')

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


b,g,r = cv2.split(cat)
img = cv2.merge((b,g,r))
cat1 = cat.copy()
cat1[:,:,0] = 165
cat1[:,:,1] = 155
cat1[:,:,2] = 145
cv_show('image',cat1)