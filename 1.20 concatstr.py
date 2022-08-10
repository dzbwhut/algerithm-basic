# 拼接最小字符串：课程列表_牛客网
# https://www.nowcoder.com/study/live/718/1/20
str = 'a a a a a a a a a aa a a a a a a a a a a a a a aabmcy a aba aa a a a aa a a a a a a a a a a a aak a a a aa a abpwv a aeib a ab a a a a a a a a a a a a a a a a a a a a aal a a a a a a a a a a a a aa aaikwc a a a aann a aao ab abecc a abk a a a aa abkpna a a a a a a a a a a a a aaf a aasiw a a a a aa aa a aa aaht a a a a a a a a a a aahdfg a aazbcqf a a a a a a a aarxft a a a a a a a a a a aa aaoil a aaqsrp a a a a a aaaxc a ab abfnc ab abmc abhhfy ab aayixkd abk abjrwj ablm aaia abscn abtbhqo abmp abu abwid a a a aab a abn aakhsfz a abj a abx abukgr actfs acx acqnhb a abacw aco a a abuki a a a a a a a a a a a abevy aamd a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a aaltv a aaue aauf a abbbev aag a a a a a a a a a a a a a a a a a a aahtz a abiwvw abmqgp aax abj aar abnd abzna ac abt abo accybv ac acklqb abbq aaf acg aciccw abkxf actau a adgeja ad aci aaoeuxz adghrb aapoawu aai ac a a aal a ab a a a a a a a ac a a a a a a a a a a a a a aahfqg aawmejm a a a a a aamq a aaoe abntif aaqwfb aan a a a a a a a a a a a a a a a a a a aaqjxc a a a a a aas a abkfhtg ab abnkd a adv acahtch acop aclt aclccwd acqx ad ad acyutsm adqgdrl adhmt adexhf acfikiu adflo abq adrcrok adrz ady adr ae aeeoydv aehraca aejjfbf acosdos adnwd adbkt ae abq aejso aehwqt aemnhr aeu aesrwg adkga ac aevvzt aewq afbfpsn a afbmaia adcfgr aev afhm ad a a a a a a a a a a a a a a a a aajbntr aasc a ab a abbj aasn a aawtl abgd a a a a a a a a a a a a a a aah a a a a a a a a aazvfg aawwvyw abd a a a a a a a a a a a a a a aap aas a ab ab a a abn a a aabzo a a a a a aalbr a a a a abcbz a abocihs ablfo act aget abfz a abxdew abq aceym a a a a a abg a aasfho a aawbny a aaxklhj a abpzato aavb abqsvuf a a a a a a a a aavo a aaxg a aa a a a aahksnj abngbq a acha abjr aabnuu aahquod aajh aahs abjyt a a a a a a aaxvy a a ac a a a aa a aan a a a a a a a abowkf ac a a aadt a aaqi ab ab a abiac a a a a a aaltrq abb a a a a a a a a a aa a a aa a a aavftb a aacalgj a a a a a a'.split(
)

str = 'a a aabmcy a aba aa aak aaaa aacalgj aaaxc a a aahdfg a a a a a a aaht aei'.split(
)


def cmp_3c(s, t):
    if s > t: return 1
    elif s == t: return 0
    else: -1


def cmp_string(s, t):
    m = len(s)
    n = len(t)
    if m == n: return cmp_3c(s, t)

    k = min(m, n)
    if s[:k] != t[:k]:
        return cmp_3c(s[:k], t[:k])

    v = max(m, n)
    i, j = k % m, k % n
    for e in range(k, v):
        if s[i] == t[j]:
            i = (i + 1) % m
            j = (j + 1) % n
        else:
            break
    return cmp_3c(s[i], t[j])


def biSearch(q, s):
    id = len(q)  #队末
    if len(q) == 0:  #空队列，在队头或者队尾插入皆可
        return 0  # 队头

    l = 0
    r = len(q) - 1
    while l <= r:
        m = int((l + r) / 2)
        ans = cmp_string(s, q[m])
        if ans == 1:  #大于中值，右半查找
            l = m + 1
        elif ans == 0:  #等于时就不再循环了
            return m
        else:  #小于中值，左半查找
            r = m - 1
            id = m

    return id


q = []
for s in str:
    i = biSearch(q, s)
    q.insert(i, s)
'''
n = int(input())
q = []
for i in range(n):
    s = input()
    i = biSearch(q, s)
    q.insert(i, s)
    '''

for e in q:
    print(e, end=' ')
print('\n')

dsaaaxcaabaabmcyaabnuuaabwqlaabzoaacalgjaadtaaexcaafaafaagaagaagkzvjaagzlaahaahdfg
dsaaaxcaabaabmcyaabnuuaabwqlaabzoaacalgjaadtaaexcaafaafaagaagaagkzvjaagzlaahaahdfgaahfqgaahksnjaahquodaahraahsaahslaahtaahtzaaiaaiaaaikwcaaiyqla