#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : 1.14 waterOnLandform.py
@Time    : 2022/01/07 22:10:55
@Author  : dzb
@Contact : dzbwhut@163.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : 地形盛水：
    题    目:   如果给你一个二维数组，每一个值表示这一块地形的高度，求整块地形能装下多少水。
        输入描述:  第一行输入两个数，M，N,M<=100,N<=100
                接下来M行，每行输入N个数，第i行ii列的数表示（i,ii）位置处地形的高度，a[i][ii]<=100  
        输出描述:  输出一个数，表示整块地形能装下多少水
            示例1  输入:    3 5
                            5 5 5 5 5
                            5 3 1 4 5
                            5 5 5 5 5 
                    输出:   7 
            示例2   输入:   10 10
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
    题    解：  木桶效应，最短的木桶块--决定--能盛的水量；
                用小根堆获取并更新“最低沿”，计算4邻域蓄水量。
                
    步    骤：  1) 周边的“高度与坐标” --入--> 小根堆；
                2）while 堆 != 空：                   
                3) 弹出-->洼地，更新洼地高度：most=max(most,h)
                4) 洼地4邻域入堆：
                    if 邻接点(坐标)合法 and 未被访问过：
                        a、if 邻接点高度h<most,then 能容水：most-h;
                        b、邻接点-->入堆
                5) 跳转2)
'''
import heapq

def getWaterLandform(n, mat):
    R,C=n 
    f=[[1 for i in range(C)] for j in range(R)] #访问标志 1-可访问(未访问的元素) 0--不可访问（已访问过的）    
    tasks=[]   
    w=0    
    # 4邻域坐标偏移量 
    X=[1,-1,0,0]
    Y=[0,0,1,-1]
    
    r=R-1
    for i in range(0,C):
        heapq.heappush(tasks,(mat[0][i],0,i))
        f[0][i]=0
        heapq.heappush(tasks,(mat[r][i],r,i))
        f[r][i]=0
        
    c=C-1
    for i in range(0,R):
        heapq.heappush(tasks,(mat[i][0],i,0))
        f[i][0]=0
        heapq.heappush(tasks,(mat[i][c],i,c))
        f[i][c]=0
    
    most=0
    while tasks: # 
        v,r,c = heapq.heappop(tasks)
        most = max(most,v)
        for i in range(0,4):
            x,y = c+X[i],r+Y[i]            
            if x>=0 and x<C and y>=0 and y<R and f[y][x]==1:
                w += max(0,most-mat[y][x])
                f[y][x] = 0
                heapq.heappush(tasks,(mat[y][x],y,x)) 
                     
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
