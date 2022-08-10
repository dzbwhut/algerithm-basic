'''s = input().split()
n, root = int(s[0]), int(s[1])
T = [[0, n, root]]
'''


def biSearch(T, l, r, v):
    id = l
    if l == len(T):
        return id

    while l <= r:
        m = int((l + r) / 2)

        id = m
        if v == T[m][0]:
            break
        elif v < T[m][0]:
            r = m - 1
        else:
            l = m + 1
    if v > T[r][0]:
        id = r + 1
    return id


def maxSearchTree(T, r):
    if T[r][1] == 0:
        lf, isSTrLf, extremumLf = 0, 1, [T[r][0],T[r][0]]
    else:
        lf, isSTrLf, extremumLf = maxSearchTree(T, T[r][1])
        

    if T[r][2] == 0:
        rt, isSTrRt, extremumRt = 0, 1, [T[r][0],T[r][0]]
    else:
        rt, isSTrRt, extremumRt = maxSearchTree(T, T[r][2])

    if T[r][1] == 0 and T[r][2] == 0:
        return [1, 1,[T[r][0],T[r][0]]]
    elif isSTrLf == 1 and isSTrRt == 1 and extremumLf[1] <= T[r][0] and (
            T[r][0] <= extremumRt[0] or T[r][2] == 0):
        return [lf + rt + 1, 1,[extremumLf[0],extremumRt[1]]]
    else:
        return [max(lf, rt), 0,[-1,-1]]


'''
for i in range(n):
    s = input().split()
    node = [int(e) for e in s]
    #j = biSearch(T,1,i,node[0])
    #T.insert(j, node)
    T.append(node)'''
S = '''0 38 30
30 15 27
15 0 34
34 20 28
20 11 0
11 1 0
1 0 0
28 8 35
8 5 3
5 6 18
6 16 0
16 0 0
18 0 0
3 0 0
35 38 0
38 13 0
13 4 2
4 0 0
2 0 0
27 26 25
26 32 22
32 0 0
22 0 21
21 23 0
23 0 0
25 0 19
19 0 9
9 0 17
17 37 12
37 0 33
33 0 36
36 10 0
10 29 31
29 0 0
31 0 7
7 0 0
12 0 24
24 14 0
14 0 0
'''
'''0 49 31
31 48 30
48 11 19
11 39 0
39 0 43
43 0 0
19 8 0
8 28 0
28 0 15
15 6 0
6 0 23
23 1 0
1 0 0
30 38 46
38 49 40
49 0 16
16 2 27
2 29 0
29 0 0
27 0 0
40 17 24
17 13 21
13 0 0
21 12 20
12 0 0
20 37 0
37 10 0
10 0 0
24 0 0
46 32 44
32 45 7
45 0 0
7 26 9
26 0 3
3 33 22
33 18 0
18 0 25
25 0 35
35 0 0
22 0 0
9 0 5
5 14 47
14 41 36
41 0 0
36 0 0
47 34 42
34 0 0
42 0 0
44 0 4
4 0 0
'''
'''0 38 30
30 15 27
15 0 34
34 20 28
20 11 0
11 1 0
1 0 0
28 8 35
8 5 3
5 6 18
6 16 0
16 0 0
18 0 0
3 0 0
35 38 0
38 13 0
13 4 2
4 0 0
2 0 0
27 26 25
26 32 22
32 0 0
22 0 21
21 23 0
23 0 0
25 0 19
19 0 9
9 0 17
17 37 12
37 0 33
33 0 36
36 10 0
10 29 31
29 0 0
31 0 7
7 0 0
12 0 24
24 14 0
14 0 0
'''
#S =
'''0 3 1
1 0 3
3 2 0
2 0 0 
'''
#S =
'''0 42 1
1 17 19
17 31 35
31 0 0
35 20 38
20 18 28
18 0 0
28 0 0
38 3 6
3 7 10
7 0 16
16 30 42
30 0 41
41 0 0
42 0 0
10 0 0
6 40 5
40 21 8
21 4 0
4 0 0
8 0 0
5 0 29
29 25 27
25 0 26
26 0 0
27 0 0
19 39 32
39 33 0
33 22 13
22 36 11
36 0 9
9 0 0
11 0 0
13 12 0
12 0 0
32 23 15
23 14 37
14 2 34
2 0 0
34 0 0
37 24 0
24 0 0
15 0 0
'''
S = S.split('\n')
T = []
for e in S:
    Li = [int(i) for i in e.split()]
    T.append(Li)
T.pop(-1)
root = T[0][2]
T = sorted(T, key=lambda key: key[0])
m, _, _= maxSearchTree(T, root)
print(m)