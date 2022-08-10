import numpy as np
a=np.array([[1.,2.],[3.,4.]])
c=np.divide(a,a) #矩阵点除

#print("[矩阵点除]divide(a,a)=\n",c)

A=np.mat([[1.,2.],[3.,4.]])
C=np.divide(A,A) #矩阵点除

#print("[矩阵点除]divide(A,A)=\n",C)

a  = np.asmatrix(np.ones([2,3]))
b = np.asmatrix(np.ones([3,3]))
b[1,1] = 5
b[0,2]=3
b[2,2] = 2
print(b,'\n')
print(b.I)