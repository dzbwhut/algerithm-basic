#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : 1.14 waterOnLandform.py
@Time    : 2022/01/07 22:10:55
@Author  : dzb
@Contact : dzbwhut@163.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : None

54  6 58 11 80 56 75 53 48  7
58 47 29 77 47 36 46 44 87 12
57 15 90 41 18 78 80 66 96 89
 6 14 59 15 83 39 21 89  8 22
34 84 49 41 38 53 42 40 54 72
89  0 89 55 27 97 49 80 28 57
40  8 74 34 92 17 23  0 14 10
48 67 42 25 69 52 60 78 81 73
89 30 80 22 18 83 52 49 20 46
48 29 47 64 64 75 56 61 56 73

[[54,  6, 58, 11, 80, 56, 75, 53, 48,  7], 
 [58, 47, 47, 77, 47, 46, 46, 46, 87, 12], 
 [57, 15, 90, 41, 41, 78, 80, 66, 96, 89], 
 [ 6, 14, 59, 41, 83, 39, 39, 89, 22, 22], 
 [34, 84, 49, 41, 38, 53, 42, 42, 54, 72], 
 [89,  8, 89, 55, 38, 97, 49, 80, 28, 57], 
 [40,  8, 74, 34, 92, 23, 23, 14, 14, 10], 
 [48, 67, 42, 25, 69, 52, 60, 78, 81, 73], 
 [89, 30, 80, 22, 22, 83, 52, 49, 46, 46], 
 [48, 29, 47, 64, 64, 75, 56, 61, 56, 73]]

54  6 58 11 80  
58 47 29 77 47  
57 15 90 41 18  
 6 14 59 15 83
 
3 5
5 5 5 5 5
5 3 1 4 5
5 5 5 5 5 
'''

import sys 

def minPos(n, mat,f):
    #四周最低处
    # 非最低的标识访问过
    M,N=n 
    hmin=100
    posmin=[0,0]
    rb=M-1 
    cr=N-1    
    for i in range(N):
        if mat[0][i]<hmin: # row--top
            hmin=mat[0][i]
            posmin=[0,i]
        f[0][i]=0
        if mat[rb][i]<hmin: # row--bottom
            hmin=mat[rb][i]
            posmin=[rb,i]
        f[rb][i]=0 
        if  i>0 and i<M-1:
            if mat[i][0]<hmin: # col--left
                hmin=mat[i][0]
                posmin=[i,0]
            f[i][0]=0              
            if mat[i][cr]<hmin: # col--right
                hmin=mat[i][cr]
                posmin=[i,cr]
            f[i][cr]=0   
                       
    return [hmin,posmin,f]

def N4min(n,mat,pnt,en=0,f=[]):
    p4=[]#4邻域
    r,c=pnt
    M,N=n
    if (r>0):      p4.append([r-1,c])
    if (r<M-1):    p4.append([r+1,c])
    if (c>0):      p4.append([r,c-1])
    if (c<N-1):    p4.append([r,c+1])
    min=1000
    pos=[-1,-1]
    for rn,cn in p4:
        if mat[rn][cn]<min:
            if en==1: 
                if f[rn][cn]==1:
                    min=mat[rn][cn]
                    pos=[rn,cn]
            else:
                min=mat[rn][cn]
                pos=[rn,cn]
                
    return p4,min,pos

def neib4(n, mat,gmin,f,vs, w):
    M,N=n
    r,c=vs.pop() 
    
    p4,min,posmin=N4min(n,mat,[r,c])
    
    if mat[r][c]<gmin: 
        w += gmin-mat[r][c]
        mat[r][c]=gmin     
             
    if mat[r][c]<min:
        w += min-mat[r][c]
        mat[r][c]=min
    f[r][c]=0
        
    # 4邻域访问 
    for r,c in p4:  
        if f[r][c]==1 and [r,c] not in vs:
            vs.insert(0,[r,c])    
    
    return w, mat,f,vs

def getWaterLandform(n, mat):
    M,N=n       
    if M<2 or N<2: 
        return 0
    
    f=[[1 for i in range(N)] for j in range(M)] #访问标志 1-可访问(未访问的元素) 0--不可访问（已访问过的）    
        
    #四周最低处
    gmin,posmin,f = minPos(n, mat,f)   
    i=0
    en=0    
    while True: 
        p4,min,posmin=N4min(n,mat,posmin,en,f)
        en=1
        r,c=posmin
        i+=1
        if f[r][c]==1:
            break
        if i>=M*N:
            return 0
        
    vs=[posmin]    
       
    #从最低点开始四邻域访问
    # 洼地蓄水
    w = 0    
    while len(vs)>0:
        w, mat,f,vs = neib4(n, mat,gmin,f,vs,w)
    
    print(mat)
    # 洼地总体涨水    
    return w

data1='''   3 5
            5 5 5 5 5
            5 3 1 4 5
            5 5 5 5 5 '''
data2='''   10 10
            54  6 58 11 80 56 75 53 48  7
            58 47 29 77 47 36 46 44 87 12
            57 15 90 41 18 78 80 66 96 89
            6 14 59 15 83 39 21 89  8 22
            34 84 49 41 38 53 42 40 54 72
            89  0 89 55 27 97 49 80 28 57
            40  8 74 34 92 17 23  0 14 10
            48 67 42 25 69 52 60 78 81 73
            89 30 80 22 18 83 52 49 20 46
            48 29 47 64 64 75 56 61 56 73'''
            
if __name__=="__main__":    
    n=[]
    mat =[]
    i=0  
    data=data2.split('\n')
    for line in data:
        if line=='\n':
            break
        
        strLst=line.split()
        i+=1
        
        arr = [int(s) for s in line.split()]
        if i%2 == 1 and len(arr) == 2:
            n=arr
        else:        
            mat.append(arr)
            
    print(getWaterLandform(n,mat))

