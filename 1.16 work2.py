'''找工作: a、有序表；能力值升序，薪资降序；
  b、剔除：1）同力低薪；2）升力降薪；
    (实现：删除薪资非升序岗位)
  c、查找：二分法：递归，迭代

  为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是
  在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。

  输入描述:
    每个输入包含一个测试用例。
    每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
    接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
    接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
    保证不存在两项工作的报酬相同。
  输出描述:
    对于每个小伙伴，在单独的一行输出一个整数表示他能得到的最高报酬。如果他找不到工作，则输出0。一个工作可以被多个人选择。
    示例1
    输入
    3 3 
    1 100 
    10 1000 
    1000000000 1001 
    9 10 1000000000 
    输出
    100 
    1000 
    1001 
    '''
'''
    st = input().split()
    n, m = int(st[0]), int(st[1])  #0--能力，1--薪资

    works = []
    for i in range(n):
        st = input().split()
        w = [int(s) for s in st]
        works.append(w)
    '''
#from typing_extensions import runtime_checkable

n = 13
m = 19
works = [[7, 10], [8, 11], [9, 10], [35, 39], [12, 12], [28, 28], [32, 27],
         [12, 19], [16, 24], [24, 23], [41, 39], [41, 40], [35, 40]]

ables = [
    46, 14, 68, 24, 7, 10, 41, 57, 15, 17, 29, 26, 27, 10, 21, 35, 38, 67, 76
]


#去除无效职位
def rmInvalidWorks1(works):
    b, i = [0, 0], 0
    for j in range(len(works)):
        # 同力底薪
        if works[i][0] > b[0]:  #力大
            if works[i][1] > b[1]:  #薪高，职位保留
                b = works[i]  #更新基准
                i += 1
            else:  #薪不高，移除职位
                del works[i]  #??@dzb
        elif works[i][0] == b[0]:  #力同，薪不大(力升序，薪降序)
            del works[i]
    return works


#去除无效岗位: 力升序且薪降序时，去除薪资非升序的岗位。
# 注意数据特点。
def rmInvalidWorks2(works):
    B = []
    _max = 0
    for w in works:
        if w[1] > _max:  #力大
            B.append(w)
            _max = w[1]
    return B


def binarySearch1(arr, l, r, x):  #递归
    if l >= r:
        if x >= arr[r][0]: return r
        else: return r - 1
    else:
        m = int((l + r) / 2)
        if x == arr[m][0]:
            return m
        elif x < arr[m][0]:
            return binarySearch1(arr, l, m - 1, x)
        else:
            return binarySearch1(arr, m + 1, r, x)


def binarySearch2(arr, l, r, x):  #迭代
    ans = -1
    while r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid][0] <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
            pass
    return ans


def binarySearch3(arr, l, r, x, key=lambda x: x):  #迭代
    ans = -1
    while r >= l:
        mid = int((l + r) / 2)
        if key(arr[mid]) <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
            pass
    return ans


''' 控制台输入：工作集，应聘人(能力)集
    # 输入：工作集
    st = input().split()
    n, m = int(st[0]), int(st[1])
    works = []
    for i in range(n):
        st = input().split()
        w = [int(s) for s in st]
        works.append(w)

    #输入：应聘人能力
    st = input().split()
    ables = [int(s) for s in st]
    '''

works = sorted(works, key=lambda work: work[1], reverse=True)
works = sorted(works, key=lambda work: work[0])

B = rmInvalidWorks2(works)

for a in ables:
    i = binarySearch3(B, 0, len(B) - 1, a, key=lambda e: e[0])
    v = B[i][1] if i >= 0 else 0
    print(v)