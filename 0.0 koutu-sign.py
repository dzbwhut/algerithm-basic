import cv2 as cv
import numpy as np

imgname='C:\\Users\\Administrator\\Pictures\\sign-1.jpg'
I=cv.imread(imgname)
b,g,r = cv.split(I)
G3=cv.merge((g,g.copy(),g.copy()))
R3=cv.merge((r,r.copy(),r.copy()))
bgro=np.hstack((I,R3,G3))
cv.imshow('o-g-r',bgro)
cv.waitKey(1)
#获取图像的大小
#thr=185
thr=220
h,w=I.shape[:2]
mask=np.zeros([h,w],dtype=np.int8)
I4=np.zeros([h,w],dtype=np.int8)
#In=[I4[:,0:2,:].copy(), I4[:,0:2,:].copy(), I4[:,0:2,:].copy()]

t=0
#for k in range(1,(12+1)):  
for k in range(1,(3+1)):
  thr += 10
  if thr!=190: 
    I4=np.zeros([h,w],dtype=np.uint8)

  for i in range(h):
    for j in range(w):       
      if I[i][j][0]>thr and I[i][j][1] >thr and I[i][j][2]>thr :
        #I4[i][j][0],I4[i][j][1],I4[i][j][2],I4[i,j,3]=255,255,255,255 
        I4[i][j]=255
      '''      
      if  (I[i][j][0]-I[i][j][2])>thr and (I[i][j][0]-I[i][j][1]) >thr:
        #I4[i][j][0],I4[i][j][1],I4[i][j][2],I4[i,j,3]=255,255,255,255
        I4[i][j]=255  
        '''
      #else:
        #I4[i][j][1],I4[i][j][2],I4[i][j][3]=I[i][j][0],I[i][j][1],I[i][j][2]

  #透明通道mask与RGB通道合并成4通道的png图像
  #I4[:,:,3]=mask  #I4[:,:,0:3]=I  
  
  In=np.hstack((I4,b,g,r))  
  if k%4==0:
    t+=1
  #cv.destroyAllWindows()
  cv.imwrite('C:\\Users\\Administrator\\Pictures\\sign\\sign-'+str(thr)+'.png',I4)

  cv.imshow(str(t),In)
  cv.waitKey(0)

np.vstack((In[0],In[1],In[2]))
cv.waitKey(1)