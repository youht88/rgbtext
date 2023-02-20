import cv2
#import paddleocr
# 读取图像
image = cv2.imread('1.jpg')
#ocr = paddleocr.OCR()

# 将图像转换为HSV颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # 提取红色通道
lower_1 = (0, 100, 100)
upper_1 = (10, 255, 255)
mask_red1 = cv2.inRange(hsv_image, lower_1, upper_1)

lower_2 = (160, 100, 100)
upper_2 = (180, 255, 255)
mask_red2 = cv2.inRange(hsv_image, lower_2, upper_2)

# # 提取蓝色通道
lower_1 = (100, 100, 100)
upper_1 = (130, 255, 255)
mask_blue1 = cv2.inRange(hsv_image, lower_1, upper_1)

lower_2 = (100, 100, 100)
upper_2 = (130, 255, 255)
mask_blue2 = cv2.inRange(hsv_image, lower_2, upper_2)

mask_red = cv2.bitwise_or(mask_red1, mask_red2)
mask_blue = cv2.bitwise_or(mask_blue1, mask_blue2)

# 进行形态学操作
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)

# 检测文本区域
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours_red:
    area = cv2.contourArea(cnt)
    print(area)
    if area < 100:
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 1)
    #识别文字
    # # 提取矩形区域
    # roi = image[y:y+h, x:x+w]
    # # 将矩形区域传递给Tesseract OCR引擎进行识别
    # text = pytesseract.image_to_string(roi,config="--psm 6") 
    # print(text)   

contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours_blue:
    area = cv2.contourArea(cnt)
    print(area)
    if area < 100:
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 1)
    #识别文字
    # # 提取矩形区域
    # roi = image[y:y+h, x:x+w]
    # #将矩形区域传递给Tesseract OCR引擎进行识别
    # text = pytesseract.image_to_string(roi,config="--psm 6") 
    # print(text)   

# 显示结果
#print(ocr.ocr(image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
