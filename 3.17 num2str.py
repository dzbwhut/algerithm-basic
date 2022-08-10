#s = input()
# 字符串转换: https://www.nowcoder.com/study/live/718/3/17
'''一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
输入描述:12可以解码成“AB”，“L”这两种
输出描述: 解码方法的总数 '''

def num2str(ss,p,sm):
    n=len(ss)
    cnt=0
    if p>=n:
        return 0
    
    if s[p] in sm: 
        print(s[p])
        cnt+=num2str(ss,p+1,sm)
        
    if p<n-1 and s[p:p+2] in sm:  
        print(s[p:p+2])       
        cnt+=num2str(ss,p+2,sm)
        
    return cnt
s='226'
n = 0
m = len(s)
sm=[str(i)  for i in range(1,27)]

print('rel',num2str(s,0,sm))