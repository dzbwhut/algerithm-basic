# 二叉树权值和最大路径 牛客网https://www.nowcoder.com/study/live/718/2/9

#1、recursion
n = int(input())
bt = []
for i in range(n):
    s = input().split()
    bt.append([int(s[0]), -1, -1])  # node: weight, lc_addr,rc_addr
    pi = int(s[1]) - 1
    if pi >= 0:
        if bt[pi][1] == -1: bt[pi][1] = i  #lc
        else: bt[pi][2] = i  #rc


def getMaxLongestPathOfBiTree(BT, i):
    wl, wr = 0, 0
    if BT[i][1] > 0:
        wl = getMaxLongestPathOfBiTree(BT, BT[i][1])

    if BT[i][2] > 0:
        wr = getMaxLongestPathOfBiTree(BT, BT[i][2])

    return BT[i][0] + max(wl, wr)


print(getMaxLongestPathOfBiTree(bt, 0))

# 2 iteration
n = int(input())
w = [0 for _ in range(n)]
_max = 0
for i in range(n):
    s = input().split()
    w[i] = int(s[0])  # 当前权重
    pi = int(s[1]) - 1
    if pi >= 0:  #子节点权重+父权重
        w[i] += w[pi]
    if _max < w[i]:
        _max = w[i]
print(_max)