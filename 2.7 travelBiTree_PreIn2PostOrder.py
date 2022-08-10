'''二叉树遍历：  已知先序和中序求后序 牛客 https://www.nowcoder.com/study/live/718/2/7
    题解：递归    
        
    题目: 给出一棵二叉树的先序和中序数组，通过这两个数组直接生成正确的后序数组。
        输入描述:
            第一行一个整数 n，表示二叉树的大小。
            第二行 n 个整数 a_i，表示二叉树的先序遍历数组。
            第三行 n 个整数 b_i，表示二叉树的中序遍历数组。
        输出描述:
            输出一行 n 个整数表示二叉树的后序遍历数组。
        示例1
            输入
            3
            1 2 3
            2 1 3 
            输出
            2 3 1    '''
'''
n = int(input())
a = input().split()
a = [int(s) for s in a]
b = input().split()
b = [int(s) for s in b]
'''
a = [[1, 2, 3], [1, 2, 4, 8, 9, 5, 10, 13, 14, 3, 6, 11, 15, 7, 12, 16]]
b = [[2, 1, 3], [8, 4, 9, 2, 13, 10, 14, 5, 1, 6, 11, 15, 3, 7, 16, 12]]
c = [[2, 3, 1], [8, 9, 4, 13, 14, 10, 5, 2, 15, 11, 6, 16, 12, 7, 3, 1]]


def travelBiTree_PreIn2PostOrder(a, b):
    # 边界值控制
    if len(a) == 0:
        return []
    elif len(a) == 1:
        return a
    elif len(a) == 2:
        return [a[1], a[0]]

    i = b.index(a[0])
    lf = travelBiTree_PreIn2PostOrder(a[1:i + 1], b[:i])
    rt = travelBiTree_PreIn2PostOrder(a[i + 1:], b[i + 1:])
    lf += rt
    lf.append(a[0])
    return lf


for i in range(2):
    p = travelBiTree_PreIn2PostOrder(a[i], b[i])
    n = len(a[i])
    print('\n', i, ")------------")

    for j in range(n):
        print(c[i][j], ' ', p[j])
