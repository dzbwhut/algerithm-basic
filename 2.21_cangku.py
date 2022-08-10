def getMinCost(lst, cnt, max_id):

    if cnt <= 0: return [0, 0]
    elif cnt == 1: return [lst[0], 0]

    lf, rt = 0, cnt - 1
    while lst[lf] == 0:
        lf += 1
    while lst[rt] == 0:
        rt -= 1

    if lf > rt: return [0, 0]
    elif lf == rt: return [lst[lf], lf]
    '''
    k=int((lf+rt)/2);
    re=(lf+rt)%2;
    if re==0 and max_id<k:
        mid=k;
    else: mid=k+1;
    
    #搜索范围：mid-1:mid+1,需要扩大范围不？
    #
    lf = (mid-1) if mid-1>=0 else 0
    rt = (mid+2) if mid+1<cnt else cnt
    '''

    min_rs, min_id = 1000, 0
    for i in range(lf, rt+1):
        cur_rs = 0
        for j in range(cnt):
            cur_rs += lst[j] * abs(i - j)

        if min_rs > cur_rs:
            min_rs = cur_rs
            min_id = i

    return [min_rs, min_id]

def getCost(mat, m, n):
    ct = 0
    rs = [0] * m
    cs = [0] * n
    rs_mx, rs_id = 0, 0
    cs_mx, cs_id = 0, 0

    for i in range(m):
        rs[i] = sum(mat[i])
        if rs[i] > rs_mx:
            rs_mx = rs[i]
            rs_id = i
    ct_r = getMinCost(rs, m, rs_id)

    for j in range(n):
        col = [r[j] for r in mat]
        cs[j] = sum(col)
        if cs[j] > cs_mx:
            cs_mx = cs[j]
            cs_id = j
    ct_c = getMinCost(cs, n, cs_id)

    return ct_r[0] + ct_c[0]


'''
T = int(input())

for i in range(T):
    s = input().split()
    n, m = [int(e) for e in s]
    mat = [[]] * m
    for j in range(m):
        s = input().split()
        r = [int(_) for _ in s]
        mat[j] = r
    ct = getCost(mat, m, n)
    print(ct)'''

input = '''3
2 2
1 1
1 0
4 4
0 8 2 0
1 4 5 0
0 1 0 1
3 9 2 0
6 7
0 0 0 0 0 0
0 1 0 3 0 1
2 9 1 2 1 2
8 7 1 3 4 3
1 0 2 2 7 7
0 1 0 0 1 0
0 0 0 0 0 0'''

k = 0
s = input.split('\n')
T = int(s[k])
for i in range(T):
    k += 1
    ds = s[k].split()
    n, m = [int(e) for e in ds]
    mat = [[]] * m
    for j in range(m):
        k += 1
        ds = s[k].split()
        r = [int(_) for _ in ds]
        mat[j] = r
    ct = getCost(mat, m, n)
    print(ct)