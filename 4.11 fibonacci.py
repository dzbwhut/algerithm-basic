''' fibonacci数列: 1,1,2,3,5,8,11,...，  通项公式：1）F(n)=F(n-1)+F(n-2),  2）且F(1)=1,F(2)=1;
    解析：特点 1)无条件转移，2) 有固定初值 ==> 算法复杂度O(logN)
    推导：

    '''
import numpy as np
import math
import time
# n=int(input())

def fibonacci(n):
    if n>0 and n<3:
        #print(1)
        return 1
    else:
        M=np.mat([[1,1],[1,0]])
        res=np.eye(M.shape[0])
        Mi=np.copy(M)
        b=n-2
        finit=np.mat([1,1])
        while(b>0):            
            if b&1:
                res=np.matmul(res,Mi)
            
            Mi=np.matmul(Mi,Mi) 
            b>>=1
            #print(i)

        fn = finit * res
        #print(fn)
        return int(fn[0,0]%(1e9+7))

def fibonacci_0(n):
    if n>0 and n<3:
        #print(1)
        return 1
    else:
        a,b=1,1
        for i in range(3,n+1):
            c=int((a+b)%(1e9+7))
            a=b 
            b=c 
        return c       

#if __function__=="__main__":
i=0xffffe
start=time.time()
r=fibonacci(i)
end=time.time()
print(r,'   t(ms): ',(end-start)*1000)

start=time.time()
r=fibonacci_0(i)
end=time.time()
print(r,'   t(ms): ',(end-start)*1000)

ra=[]
rb=[]
for i in range(10):
   ra.append(fibonacci(i+1))
   rb.append(fibonacci_0(i+1))
print(ra,'\n',rb)
            