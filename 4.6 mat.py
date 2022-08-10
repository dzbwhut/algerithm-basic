#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param mat int整型二维数组 
# @param n int整型 
# @param m int整型 
# @param x int整型 
# @return int整型一维数组
#
from data_4_6 import *

class Solution:
    #def findElement(self , mat: list[list[int]], n: int, m: int, x: int) -> list[int]:
    # 有bug:依赖严格单调：行列同时单调：
    def findElement_1(self , mat, n, m, x):
        # write code here
        if mat[0][1]>mat[1][0]:
            k = m - 1
            for i in range(1,m):
                if(x<mat[0][i]):
                    k=i-1
                    break
                elif x==mat[0][i]:
                    return [0,i]

            for i in range(0,n):
                if(x==mat[i][k]):
                    return [i,k]
        else:
            k=n-1
            for i in range(1,n):
                if(x<mat[i][0]):
                    k=i-1
                    break
                elif x==mat[i][0]:
                    return [i,0]

            for i in range(0,m):
                if(x==mat[k][i]):
                    return [k,i]
    
    def findElement_2(self , mat, n, m, x):
        # write code here 左下角，右上角，严格单调       
        r,c=0,m-1
        while(r<n and c>=0):
            if x==mat[r][c]:
                return [r,c]
            elif x<mat[r][c]:
                c-=1
            else:
                r+=1
        return [-1,-1]

    # 二分查找
    def findElement_3(self , mat, n, m, x):
        # write code here        
        r,c=0,m-1
        while(r<n and c>=0):
            if x==mat[r][c]:
                return [r,c]
            elif x<mat[r][c]:
                c-=1
            else:
                r+=1
        return [-1,-1]    
solt=Solution()
#mat=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#n=5
#m=5
#x=24
print(solt.findElement_2(mat,n,m,x))