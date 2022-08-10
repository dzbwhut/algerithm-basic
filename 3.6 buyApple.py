'''https://www.nowcoder.com/study/live/718/3/15
'''
n = int(input())
ans = -1
if n >= 6:
    r = n % 8
    for b in range(int(n / 8), -1, -1):
        if r % 6 == 0:
            ans = b + int(r / 6)
            break
        r += 8
print(ans)