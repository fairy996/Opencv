import cv2
import matplotlib.pyplot as plt

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image1 = cv2.imread('Z_ClassTask\\task2\\output\\image_jpg_qualitymax.jpg')
image2 = cv2.imread('Z_ClassTask\\task2\\output\\image_jpg_qualitymax.png')
image3 = cv2.imread('Z_ClassTask\\task2\\output\\image_jpg_qualitymax.webp')

plt.subplot(131), plt.imshow(image1), plt.title('image_jpg_qualitymax_jpg')
plt.subplot(132), plt.imshow(image2), plt.title('image_jpg_qualitymax_png')
plt.subplot(133), plt.imshow(image3), plt.title('image_jpg_qualitymax_webp')

plt.show()