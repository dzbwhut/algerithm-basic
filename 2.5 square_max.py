'''
给定一个的矩阵matrix，在这个矩阵中，只有0和1两种值，返回边框全是1的最大正方形的边长长度、
例如
0 1 1 1 1
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 1 0 1 1
其中，边框全是1的最大正方形的大小为，所以返回4
[要求] 时间复杂度为O(n^3)，空间复杂度为O(n^2)

输入描述:
第一行一个整数N。表示矩阵的长宽。
接下来N行，每行N个整数表示矩阵内的元素

输出描述:  输出一个整数表示答案

示例1: [输入]
5
0 1 1 1 1
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 1 0 1 1 
[输出] 
4 
备注: 1≤N≤200，MATRIXi,j=0/1
'''
'''
n = int(input())
mat = []
for i in range(n):
    sLst = input().split()
    row = [int(s) for s in sLst]
    mat.append(row)'''
import numpy as np
n = input()
n = 5
mat = [[1, 1, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 1],
       [1, 1, 0, 0, 1]]
mat = np.array(mat)
s = sum(sum(mat))
t = np.sort(np.array([2, 7, 1, 4]))
#getMaxSque
#1 find ver-1
#2 if noe 1-ver edge=0 er
#3.find 1-ver:
#  3.1 while  right and down is 1-ver
#      3.1.1 while r-down and d-right 1-ver until r-d(x,y)==d-r(x,y)
#      3.1.2 else  break
s = 0
for e in mat:
    s += sum(e)

if s == 0:
    print(0)
elif s < 4:
    print(1)
elif s == n * n:
    print(n)
else:
    e_max = 1
    for i in range(n - 1):
        if i >= n - e_max:
            break
        for j in range(n - 1):
            if j >= n - e_max:
                break

            if mat[i][j] == 1:
                e = 1
                k, v = i + 1, j + 1
                isFindRD = 1
                while k > i:
                    # search bounds of right and bottom
                    if isFindRD == 1:
                        while mat[i][v] == 1 and mat[k][j] == 1:
                            e += 1
                            if k == n - 1 or v == n - 1:
                                break
                            k, v = k + 1, v + 1
                    if e > e_max:
                        erow = sum(mat[i + e - 1][j:j + e])
                        hd = [r[j + e - 1] for r in mat]
                        ecol = sum(hd[i:i + e])
                        if erow == e and ecol == e:
                            e_max = e
                            break
                        else:
                            e -= 1
                            k -= 1
                            isFindRD = 0
                    else:
                        break

    print(e_max)
