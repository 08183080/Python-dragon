"""
需求: 给你一张图像, 检测出这张图像中的圆形物体出来
方法: hough transform
Detecting Circles in Images using OpenCV and Hough Circles
ref: https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html
"""
import sys
import cv2 as cv
import numpy as np
def main(argv):
    
    default_file = 'smarties.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    
    gray = cv.medianBlur(gray, 5)
    
    
    rows = gray.shape[0]
    # 调参, 检测圆形...
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 40,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    
    circle_data = []
    cropped_images = []
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]

            # circle center
            # cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            # cv.circle(src, center, radius, (255, 0, 255), 3)

            circle_data.append((center, radius))

            x = center[0] - radius
            y = center[1] - radius
            w = h = radius * 2

            cropped = src[y:y+h, x:x+w]
            cropped_images.append(cropped)

            for i, cropped in enumerate(cropped_images):
                filename = "D:\\Python\\Python\\projects\\image-process\\tiny_circles\\" + str(i) + ".png"
                cv.imwrite(filename, cropped)

    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])