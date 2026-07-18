import cv2
import numpy as np

img = cv2.imread('example.jpg')
resize = cv2.resize(img, (800, 600))
cv2.imshow("Default Image", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


# edited
resize = cv2.resize(img, (800, 700))
brightened = cv2.add(img, np.array([60.0]))
cv2.imshow("Edited Image", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()