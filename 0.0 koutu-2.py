#coding:utf-8
import cv2
import numpy as np
#加载图片
image = cv2.imread('C:\\Users\\Administrator\\Pictures\\sign-2.png')
#统一处理图片大小
img_w = 650 if image.shape[1] > 600 else 400
image = cv2.resize(image, (img_w,int(img_w*image.shape[0]/image.shape[1])), interpolation=cv2.IMREAD_COLOR)
impng=cv2.cvtColor(image.copy(), cv2.COLOR_RGB2RGBA)
# image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
#image = cv2.imread('img\\public-2004-16-a7912dbd-72b0-4d96-9d65-70abc21940d5.png')
hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
low_range = np.array([130, 43, 46])
high_range = np.array([180, 255, 255])
th = cv2.inRange(hue_image, low_range, high_range)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
th = cv2.dilate(th, element)
index1 = th == 255
img1 = np.zeros(impng.shape, np.uint8)
img1[:,:,:] = (255, 255, 255,0)
img1[index1] = impng[index1]  # (0,0,255)
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# 创建四通道图片
#img1=topng(img1)
#img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2RGBA)
cv2.imwrite('m1.png', img1)
cv2.imshow('1', img1)
#cv2.waitKey()
# cv2.imwrite("img1.png", img1)
low_range = np.array([0, 43, 46])
high_range = np.array([9, 255, 255])
th = cv2.inRange(hue_image, low_range, high_range)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
th = cv2.dilate(th, element)
index1 = th == 255
img2 = np.zeros(impng.shape, np.uint8)
img2[:,:,:] = (255, 255, 255,0)
img2[index1] = impng[index1]
cv2.imshow('2', img2)
cv2.imwrite('m2.png', img2)
imgreal=cv2.add(img2,img1)
cv2.imwrite('m222.png', imgreal)
#cv2.waitKey()
#img31 = cv2.cvtColor(img31, cv2.COLOR_BGR2RGB)
white_px = np.asarray([255, 255, 255,255])
#black_px = np.asarray([0, 0, 0, 255])
(row, col, _) = imgreal.shape
for r in range(row):
    for c in range(col):
        px = imgreal[r][c]
        if all(px == white_px):
            imgreal[r][c] = impng[r][c]
#扩充图片防止截取部分
img4png=cv2.copyMakeBorder(imgreal, 50, 50, 50, 50,cv2.BORDER_CONSTANT, value=[255, 255, 255,0])
img2gray = cv2.cvtColor(img4png, cv2.COLOR_RGBA2GRAY)
retval, grayfirst = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY_INV)
# 再次膨胀，轮廓查找
# img6 = cv2.GaussianBlur(grayfirst, (25, 5), 0, 0)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (22, 22))
img6 = cv2.dilate(grayfirst, element)
#cv2.imshow('img4', img6)
c_canny_img = cv2.Canny(img6, 10, 10)
contours, hierarchy = cv2.findContours(c_canny_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
areas = []
for i, cnt in enumerate(contours):
    rect = cv2.minAreaRect(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    area = w * h
    ars = [area, i]
    areas.append(ars)
areas = sorted(areas, reverse=True)
print(areas)
maxares = areas[:1]
x, y, w, h = cv2.boundingRect(contours[maxares[0][1]])
temp = img4png[y:(y + h), x:(x + w)]
#高小于宽
print(temp.shape)
if temp.shape[0]<temp.shape[1]:
    #temp = cv2.resize(temp, (150, temp.shape[0]))
    zh=int((temp.shape[1]-temp.shape[0])/2)
    temp = cv2.copyMakeBorder(temp, zh, zh, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255,0])
else:
    #temp = cv2.resize(temp, (temp.shape[1], 150))
    zh = int((temp.shape[0] - temp.shape[1]) / 2)
    temp = cv2.copyMakeBorder(temp, 0,0,zh, zh, cv2.BORDER_CONSTANT, value=[255, 255, 255,0])
dst = cv2.resize(temp, (150, 150))
cv2.imshow('3', dst)
cv2.imwrite('m0.png', dst)
cv2.waitKey()