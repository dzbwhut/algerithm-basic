import numpy as np  

# Sn=(I-M^n)/(I-M) M!=I
# Sn=(1+n)n/2   M==I

MAX_MODE=1e9+7

#s=input().split()
#n,k,p=int(s[0]),int(s[1]),int(s[2])
n,k,p=3,3,3

if k==1:
    A1=1
    An=A1+ p*(n-1)  
    s=((A1+An)*n/2)%MAX_MODE
    print( int(s))
else:    
    I=np.identity(3)   
    Q=np.array([[1,k,1],[0,k,1],[0,0,1]])
    Q2=Q.copy()

    if n&1: 
        Qn=I

    t=round(np.log2(n)+.5)
    for i in range(1,t):
        n>>=1
        Q2=np.matmul(Q2,Q2)
        if n&1==1:  Qn=np.matmul(Qn,Q2)
     
       
    v = Qn[0][0]+Qn[0][1]+Qn[0][2]*p
    v %= MAX_MODE

    print(int(v))