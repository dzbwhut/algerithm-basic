arr = [[2, 1, 3], [1, 2, 3], [2, 3, 1]]


def isPreOrderBiTree(T, s, e):
    #边界值: 叶节点--是搜索二叉树
    if len(T) <= 1 or s >= e:
        return True

    #左子区，
    i = s + 1
    while i <= e and T[i] < T[s]:
        i += 1

    if i > e or isPreOrderBiTree(T, s + 1, i - 1)==False:  #左子树，
        return False

    if i == e:
        return True
    elif i < e:
        s = i
        i += 1
        while i <= e and T[i] > T[s]:
            i += 1  #右子区，
        if i >= e:
            return isPreOrderBiTree(T, s, e)  #右子树，
        else:
            return False


for a in arr:
    print(isPreOrderBiTree(a, 0, len(a) - 1))
