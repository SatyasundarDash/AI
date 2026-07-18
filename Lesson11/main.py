import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_img = image.copy()
    if (filter_type == "red_tint"):
        filtered_img[:, :, 1] = 0
        filtered_img[:, :, 0] = 0
    elif (filter_type == "blue_tint"):
        filtered_img[:, :, 1] = 0
        filtered_img[:, :, 2] = 0
    elif (filter_type == "green_tint"):
        filtered_img[:, :, 0] = 0
        filtered_img[:, :, 2] = 0
    elif (filter_type == "increase_red"):
        filtered_img[:, :, 1] = cv2.add(filtered_img[:, :, 2]) # increase red channel
    elif (filtered_img == "decrease_blue"):
        filtered_img[:, :, 0] = cv2.subtract(filtered_img[:, :, 0], 50)
    return filtered_img

image_path = 'example.jpg'
img = cv2.imread(image_path)

if (img is None):
    print("ERROR: No image found.")
else:
    filter_type = "original"

    print("""
    Press the following keys to apply filters:
          r - Red Tint
          b - Blue Tint
          g - Green Tint
          i - Increase Red Intensity
          d - Decrease Blue Intensity
          q - Quit program.
    """)

    while True:
        filtered_img = apply_color_filter(img, filter_type)
        cv2.imshow("Filtered Image", filtered_img)

        key = cv2.waitKey(0) & 0xFF

        if (key == ord('r')):
            filter_type = "red_tint"
        elif (key == ord('b')):
            filter_type = "blue_tint"
        elif (key == ord('g')):
            filter_type = "green_tint"
        elif (key == ord('i')):
            filter_type = "increase_red"
        elif (key == ord('d')):
            filter_type = "decrease_blue"
        elif (key == ord('q')):
            print("Exiting...")
            break

        else:
            print("Invalid key! Please press a valid key.")

cv2.destroyAllWindows()

       