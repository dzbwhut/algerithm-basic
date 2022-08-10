''' 青草游戏
    牛牛和羊羊都很喜欢青草。今天他们决定玩青草游戏。
    最初有一个装有n份青草的箱子,牛牛和羊羊依次进行,牛牛先开始。在每个回合中,每个玩家必须吃一些箱子中的青草,所吃的青草份数必须是4的x次幂,比如1,4,16,64等等。不能在箱子中吃到有效份数青草的玩家落败。假定牛牛和羊羊都是按照最佳方法进行游戏,请输出胜利者的名字。
    输入描述:
    输入包括t+1行。
    第一行包括一个整数t(1 ≤ t ≤ 100),表示情况数.
    接下来t行每行一个n(1 ≤ n ≤ 10^9),表示青草份数


    输出描述:
    对于每一个n,如果牛牛胜利输出"niu",如果羊羊胜利输出"yang"。
    示例1
    输入
        3
        1
        2
        3 
    输出
        niu
        yang
        niu 


    题解：问题答案并不明确-->暴力计算：递归-->前一轮+当前--winner

    '''


def convert10_4(n: int):
    # 高位在后： 【个 十 百 。。。】
    fd = []
    while n > 4:
        fd.append(n % 4)
        n = n >> 2
    fd.append(n)
    return fd


def eatage(n: int):
    fd = []
    while n > 4:
        fd = convert10_4(n)
        if len(fd) > 1: n = sum(fd)
        elif len(fd) == 1: n = fd[0]
    if n == 2 or n == 0: ret = 'y'
    else: ret = 'n'
    return ret


def eatage_ans(n: int):
    n %= 5
    if n == 0 or n == 2: return 'y'
    else: return 'n'


arr = [
    125, 126, 127, 128, 129, 130, 131, 660629754, 506782260, 362261590,
    207365657, 621599890
]
ans = ['y', 'n', 'n', 'y', 'n', 'n', 'y', 'n', 'y', 'y', 'y', 'y']
ans2 = [
    'y', 'n', 'y', 'n', 'n', 'y', 'n', 'y', 'n', 'n', 'y', 'n', 'y', 'n', 'n',
    'y', 'n', 'y', 'n', 'n', 'y', 'n', 'y', 'n', 'n', 'y', 'n', 'y', 'n', 'n'
]
#n = int(input())
#for i in range(n):
#   m = int(input())
#   print(eatage(m))

#for i in range(len(arr)):
#print(arr[i], ' \t ', ans[i], ' \t ', eatage(arr[i]))
for i in range(61):
    ret = eatage(i)
    ans = eatage_ans(i)
    eq = ' ' if ret == ans else 'x'
    print(i, '\t', ans, '\t', eatage(i), '\t', eq)
