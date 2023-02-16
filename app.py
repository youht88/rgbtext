import cv2
import numpy as np 
import pytesseract
# 读取图像 
img = cv2.imread('1.jpg') 
# 将图像转换为灰度图像 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# 对灰度图像进行二值化 
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 
# 进行形态学处理，去除噪声和填充字符的空洞 
kernel = np.ones((5,5),np.uint8) 
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) 
# 将图像转换为HSV颜色空间 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# 设置特定颜色的范围，这里以红色为例 
lower_red = np.array([0, 100, 100]) 
upper_red = np.array([10, 255, 255]) 
mask = cv2.inRange(hsv, lower_red, upper_red) 
# 对二值图像进行OCR识别 
print(mask)
text = pytesseract.image_to_string(mask, config='--psm 6') 
# 显示图像和识别结果 
#cv2.imshow('image', img) 
#cv2.imshow('mask', mask) 
print(text) 
cv2.waitKey(0) 
cv2.destroyAllWindows()