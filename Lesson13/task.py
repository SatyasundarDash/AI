import cv2
import matplotlib.pyplot as plt


img = cv2.imread("himalaya.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rotated = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)

bright = cv2.convertScaleAbs(rotated, alpha=1.0, beta=50)
cropped = bright[100:500, 100:600]
plt.figure(figsize=(12, 8))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image"); plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bright)
plt.title("Rotated + Brightened"); plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cropped)
plt.title("Cropped Image"); plt.axis("off")

plt.tight_layout()
plt.show()