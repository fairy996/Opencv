import cv2
import matplotlib.pyplot as plt

cat = cv2.imread("F:\Deep Learning\Opencv_Study\material\liqi.jpg")
dog = cv2.imread("F:\Deep Learning\Opencv_Study\material\wenke.jpg")

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cat1 = cat + 10
cat2 = cat - 10
cat3 = cat - cat1
cv2.add(cat,cat1)
cv_show('cat',cat)
cv_show('cat1',cat1)
cv_show('cat2',cat2)

dog = cv2.resize(dog,(365,507))
dog9 = dog[0:360,0:365]
dog = cv2.resize(dog9,(365,507))
cv_show('dog',dog9)
res = cv2.addWeighted(cat,0.5,dog,0.5,0)
cv_show('res',res)

