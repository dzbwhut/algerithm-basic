n = int(input())


def getNumBitree_1(n):
    if n < 3:
        return n
    else:
        k = int(n / 2)
        r = n % 2
        s = 0
        for i in range(1, k + 1):
            if i <= 2: s1 = 1
            else: s1 = getNumBitree(i - 1)

            s2 = getNumBitree(n - i)
            s += s1 * s2
        s *= 2
        if r == 1:
            s3 = getNumBitree(k)
            s += s3**2
        return s


def getNumBitree(n):
    s = [0 for _ in range(n + 1)]
    s[:3] = [1, 1, 2]
    if n < 3:
        return s[n]

    for j in range(3, n + 1):
        k = int(j / 2)
        r = j % 2
        for i in range(1, k + 1):
            s[j] += s[i - 1] * s[j - i]
        s[j] *= 2
        if r == 1:
            s[j] += s[k]**2
        print(j, s[j])
    return s[n]


print(getNumBitree_1(n))

#print(getNumBitree(n))