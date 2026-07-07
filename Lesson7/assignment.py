# python script that resizes an img into 3 predefined sizes
import cv2, colorama
img = cv2.imread('example.jpg')
colorama.init(True)

blue = colorama.Fore.BLUE
green = colorama.Fore.GREEN
ylw = colorama.Fore.YELLOW
norm = colorama.Fore.RESET

ask = input(f"""{colorama.Fore.BLUE}Choose a number to display the image at predefined size.
           {norm} 1) {green} 800x600 - {ylw} DEFAULT RENDER,
           {norm} 2) {green} 1000x700 - {ylw} BIGGER RENDER,
           {norm} 3) {green} 600x400 - {ylw} SMALLER RENDER,
> 
""")

cv2.namedWindow('Processed Image', cv2.WINDOW_NORMAL)


sizes = [
    (800, 600),
    (1000, 700),
    (600, 400)
]

if (ask == "1"):
    cv2.resizeWindow('Processed Image', sizes[0])
    cv2.imshow('Processed Image', img)
    cv2.waitKey(0)
elif (ask == "2"):
    cv2.resizeWindow('Processed Image', sizes[1])
    cv2.imshow('Processed Image', img)
    cv2.waitKey(0)
elif (ask == "3"):
    cv2.resizeWindow('Processed Image', sizes[2])
    cv2.imshow('Processed Image', img)
    cv2.waitKey(0)


