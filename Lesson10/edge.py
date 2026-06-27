import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_img(title, image):
    plt.figure(figsize=(8,8))
    if (len(image.shape) == 2):
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactiveEdgeDetection(image_path):
    image = cv2.imread(image_path)
    if (image is None):
        print("Error: Image not found!")
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_img("Original Grayscale Image", gray_image)

    print("""Select an option:
          1. Sobel Edge Detection
          2. Canny Edge Detection
          3. Laplacian Edge Detection
          4. Gaussian Smoothing
          5. Median Filtering
          6. Exit ->
          """)
    
    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8),
                                            type(np.uint8))
            display_img("Sobel Edge Detection", combined_sobel)
        
        elif choice == "2":
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_thresh = int(input("Enter Lower threshold: "))
            upper_thresh = int(input("Enter Upper threshold: "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_img("Canny Edge Detection", edges)
        
        elif choice == "3":
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_img("Laplacian Edge Detection", 
                        np.abs(laplacian).astype(np.uint8))
        
        elif choice == "4":
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")
            kSize = int(input("Enter kernel size (odd number): "))
            blurred = cv2.GaussianBlur(image, (kSize, kSize), 0)
            display_img("Gaussian Smoothed Image", blurred)

        elif choice == "5":
            print("Adjust kernel size for Median Filtering (must be odd, default: 5)")
            kSize = int(input("Enter kernel size (odd number): "))
            medianFiltered = cv2.medianBlur(image, kSize)
            display_img("Median Filtered Image", medianFiltered)

        elif choice == "6":
            print("Exitting...")
            break 
        else:
            print('Invalid choice. Please select a number between 1 & 6.')

interactiveEdgeDetection('example.jpg')