import cv2
import numpy as np

def detect_non_black_circles(image_path):
    # 读取图片
    image = cv2.imread(image_path)
    
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 对图像进行阈值处理，将非黑色区域变为白色
    _, threshold = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    
    # 检测圆形
    circles = cv2.HoughCircles(threshold, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30, minRadius=10, maxRadius=100)
    print("!!!")

    # 提取圆形的位置和半径
    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)
        for (x, y, r) in circles:
            # 检查圆形位置对应的像素值是否非黑色
            if image[y, x, 0] != 0 or image[y, x, 1] != 0 or image[y, x, 2] != 0:
                # 绘制圆形
                cv2.circle(image, (x, y), r, (0, 255, 0), 2)
    
    # 显示结果
    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用函数进行测试
image_path = "D:\\p-dragon\\Python-dragon\\projects\\image-process\\image.jpg"
detect_non_black_circles(image_path)