#%% md
### 图像阈值

''' ret, dst = cv2.threshold(src, thresh, maxval, type)
- src： 输入图，只能输入单通道图像，通常来说为灰度图
- dst： 输出图
- thresh： 阈值
- maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
- type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV
- cv2.THRESH_BINARY:超过阈值部分取maxval（最大值），否则取0
- cv2.THRESH_BINARY_INV :THRESH_BINARY的反转
- cv2.THRESH_TRUNC :大于阈值部分设为阈值，否则不变
- cv2.THRESH_TOZERO :大于阈值部分不改变，否则设为0
- cv2.THRESH_TOZERO_INV :THRESH_TOZERO的反转
'''
import  cv2
import matplotlib.pyplot as plt

cat = cv2.imread("F:\Deep Learning\Opencv_Study\material\cat.jpg",cv2.IMREAD_GRAYSCALE)

ret, thresh1 = cv2.threshold(cat, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(cat, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(cat, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(cat, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(cat, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [cat, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

