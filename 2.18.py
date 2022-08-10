'''s = input().split()
n, root = [int(_) for _ in s]
biTree = [[n, root]]
for i in range(n):
    s = input().split()
    node = [int(_) for _ in s]
    biTree.append(node)'''

str = [
    '8 1', '1 2 3', '2 4 0', '4 0 0', '3 5 6', '5 7 8', '6 0 0', '7 0 0',
    '8 0 0'
]
biTree = [[] for _ in range(9)]
biTree[0] = [8, 1]
for i in range(1, 9):
    node = [int(_) for _ in str[i].split()]
    biTree[node[0]] = node
n, root = biTree[0]
r = [root]
for i in range(1, n + 1):
    if len(r) == 0: break
    c = []
    print('Level', i, ":", end=' ')
    for j in r:
        print(j, end=' ')
        if biTree[j][1] > 0:
            c.append(biTree[j][1])
        if biTree[j][2] > 0:
            c.append(biTree[j][2])
    print('')
    r = c

r = [root]
dr = ['from right to left:', 'from left to right:']
for i in range(1, n + 1):
    if len(r) == 0: break
    c = []
    print('Level', i, dr[i % 2], end=' ')

    for j in range(len(r)):
        if i % 2 == 1: print(r[j], end=' ')
        else: print(r[-1 - j], end=' ')

        if biTree[r[j]][1] > 0:
            c.append(biTree[r[j]][1])
        if biTree[r[j]][2] > 0:
            c.append(biTree[r[j]][2])
    print('')
    r = c