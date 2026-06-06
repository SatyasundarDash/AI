import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('example.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# to rotate

(h, w) = img.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated image")
plt.show()

# brightness 
brightness_matrix = np.ones(img.shape, dtype="uint8") * 50
brighter = cv2.add(img, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb); plt.title("Brighter Image"); plt.show()
