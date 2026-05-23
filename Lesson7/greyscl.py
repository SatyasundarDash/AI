import cv2

img = cv2.imread('example.jpg')

grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize = cv2.resize(grey_image, (800, 600))

cv2.imshow('Processed image', resize);

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('greyscale_resized_image.jpg', resize)
    print("Image saved as greyscale_resized_image.jpg")
else: print("Image not saved.")

cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resize.shape}")
