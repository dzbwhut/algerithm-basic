import PIL.Image as Image
import cv2 


def yz(imgname):
    original_image = cv2.imread(imgname)
    image = original_image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, 120, 255, 1)
 
    # 找到图片中的轮廓
    cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
 
    # 按照面积将所有轮廓逆序排序
    contours2 = sorted(cnts, key=lambda a: cv2.contourArea(a), reverse=True)
    ROI_number = 0
    for c in contours2:
        area = cv2.contourArea(c)
        print(area)
        # 只抠面积大于1200的轮廓，一般印章的轮廓面积比较大，可根据实际情况调整
        if area < 1200: break
        x, y, w, h = cv2.boundingRect(c)
        # 调整裁剪的位置，避免印章的边缘缺失
        x -= 20
        y -= 20
        w += 40
        h += 40
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 1)
        ROI = original_image[y:y + h, x:x + w]
        # cv2.imshow("ROI", ROI)
        img_name = imgname[0: imgname.rindex(".")] + '_{}.png'.format(ROI_number)
        cv2.imwrite(img_name, ROI)
        pic = Image.open(img_name)
        # 转为RGBA模式
        pic = pic.convert('RGBA')
        width, height = pic.size
        # 获取图片像素操作入口
        array = pic.load() 
        for i in range(width):
            for j in range(height):
                # 获得某个像素点，格式为(R, G, B, A)元组
                pos = array[i, j]
                # RGB三者都大于240(很接近白色了)
                isEdit = (sum([1 for x in pos[0:3] if x > 240]) == 3)
                if isEdit:
                    # 更改为透明
                    array[i, j] = (255, 255, 255, 0)
 
        # 保存图片
        pic.save(img_name)
        ROI_number += 1
        #cv2.imshow('sign-'+str(ROI_number),pic)
        #cv2.waitKey(0)

imgname='C:\\Users\\Administrator\\Pictures\\sign-2.png'
I=cv2.imread(imgname)
cv2.imshow('org',I)
cv2.waitKey(1)
yz(imgname)