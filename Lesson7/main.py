import cv2
import colorama

colorama.init(True)

img = cv2.imread('example.jpg')

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)

cv2.imshow('Loaded Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"{colorama.Fore.GREEN}Image dimensions: {img.shape}")
