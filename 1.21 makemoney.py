# 项目最大收益：课程列表_牛客网  https://www.nowcoder.com/study/live/718/1/21
''' #input
    s=input().split()
    n,w,k=int(s[0]),int(s[1]),int(s[2])
    costs=input().split()
    profits=input().split()
    '''
st = ['4 3 2', '5 4 1 2', '3 5 3 2']
s = st[0].split()
n, w, k = int(s[0]), int(s[1]), int(s[2])
costs = st[1].split()
profits = st[2].split()
#calculate
#works fiter
works = []
for i in range(n):
    works.append([int(costs[i]), int(profits[i])])

works = sorted(works, key=lambda x: x[1], reverse=True)
works = sorted(works, key=lambda x: x[0])

B = []
f = 0
for p in works:
    if p[1] > f:
        f = p[1]
        B.append(p)


def biSearch(arr, l, r, x, key):
    id = -1
    while l <= r:
        m = int((l + r) / 2)

        if x >= key(arr[m]):
            id = m
            l = m + 1
        else:
            r = m - 1
    return id


#plan works
l, r = 0, len(B) - 1
for j in range(k):
    id = biSearch(B, l, r, w, key=lambda x: x[0])
    if id >= 0: w += B[id][1]
    l = id

print(w)