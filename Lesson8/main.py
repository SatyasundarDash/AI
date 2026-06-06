import cv2
import matplotlib.pyplot as plt

img = cv2.imread('example.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("RGB Image")
plt.show()

grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

cropped_img = img[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_img)
plt.title("Cropped Region")
plt.show()

