#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : Untitled-1
@Time    : 2022/01/07 17:16:55
@Author  : dzb
@Contact : dzbwhut@163.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004x
@题目    : 数组容水: 给定一个整形数组arr，已知其中所有的值都是非负的，
                    将这个数组看作一个容器，请返回容器能装多少水。具体请参考样例解释
           输入描述:
                第一行一个整数N，表示数组长度。
                接下来一行N个数表示数组内的数。
           输出描述:
                输出一个整数表示能装多少水。
           示例1 输入:  6
                        3 1 2 5 2 4 
                 输出:  5 
题解:  两端向中间扫描计算：1) 比较左右端的值，选小端开始扫描；
        2) 小端的下一个<小端：则计算差值-->可存水，并找下一个比较；
        3）否则，更新小端ID，并调到1）继续。
'''


import sys 

def getWaterVolume( arr):
    n = len(arr)
    if n<3: 
        return 0
            
    l = 0
    r = n - 1
    w = 0
    while l <= r:
        if arr[l] <= arr[r]:
            i = l + 1
            while i <= r and arr[i] <= arr[l]:
                w += arr[l] - arr[i]
                i += 1
            l = i
        else:
            i = r - 1
            while i >= l and arr[i] <= arr[r]:
                w += arr[r] - arr[i]
                i -= 1
            r = i
    return w

n=[]
mat =[]
i=0

for line in sys.stdin:
    strLst=line.split()
    i+=1
    
    if i%2 == 1 and len(strLst) == 1:
        n.append(int(strLst[0]))
    else:
        arr = [int(s) for s in line.split()]
        mat.append(arr)
    
for arr in mat:
    print(getWaterVolume(arr))