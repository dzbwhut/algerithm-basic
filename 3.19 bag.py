# 背包问题：暴力破解-->动态规划
''' 1、题目： 牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
    牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
    牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。

    输入描述:
        输入包括两行
        第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
        第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。

    输出描述:    输出一个正整数, 表示牛牛一共有多少种零食放法。
        示例1 
            输入    3 10
                    1 2 4
            输出    8
    说明： 三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
    '''
    
'''2、题解：尝试模型： 左-->右   
        
        '''

from asyncio.windows_events import NULL
import numpy as np

def dfs(bs:list,w:int,p:int):
    cnt=0 
    if w<=0:
        return cnt
        
    for i in range(p,len(bs)):
        if bs[i]<=w:
            cnt+=1
            cnt+=dfs(bs,w-bs[i],i+1)
        else: 
            break
    if p==0:  cnt+=1 #  首次进入时，没选一物--总体积为0，也是一种选择
    
    return cnt

def dfs2(bs:list,w:int,p:int):    
    if w<0: #前次取物，容量减少到-1，说明前次取物装不下
        return -1
    
    if p>=len(bs):# 物体取完，且容量有余，
        return 1  # 此次方案可行
         
    next1=dfs2(bs,w,p+1)  # 不选当前位置的食物，容量不变：w, 则不会有:  next1==-1
    next2=dfs2(bs,w-bs[p],p+1)  # 选当前位置的食物，容量减少到:w-bs[p]
      
    if next2<0: next2=0 
    
    return next1 + next2

def dfs3(bs:list,w:int,p:int):    
    
    db=np.zeros([len(bs),w+1])
    
    for i in range(w+1):
        d
    
    return  
#s=input().split()
#n,w=int(s[0]),int(s[1])
#s=input().split()
n,w=3,5
t=[2,1,4]
s=sum(t)
if s<=w:
    k=2**n
    print(k)
else:   
    t.sort()
    for w in range(1,8):
        cnt=dfs(t,w,0)
                        
        print(w,') ',cnt)