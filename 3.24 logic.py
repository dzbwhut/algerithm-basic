''' 逻辑组合数.   f_iter有bug. f_dynamic_program, c++版OK.

    参考: https://www.cnblogs.com/grandyang/p/5271856.html 
'''

def is_valid(s):
    if len(s)&1 != 1:
        return False

    # 逻辑串S的合法性检测: n o n o ... n o n        
    for i in range(0,len(s)-1,2):
        if (s[i]=='1' or s[i]=='0') and (s[i+1]=='|' or s[i+1]=='&' or s[i+1]=='^'):
            continue
        else:
            return False

    if s[-1]=='1' or s[-1]=='0':
        return True
    else:
        return False
    
def f_iter(s:list,bv:bool)->int:    
    """Function: 产生特定逻辑值的逻辑串的计算优先级的组合数.  有bug.  

    Args: 逻辑组合数:LR范围搜索
        -s  逻辑串
        -bv 逻辑表达式的值：布尔值,True,False        

    Returns:
        int - 组合数
    """
    
    if len(s)==0:
        return 0
    elif len(s)==1:
        if s[0]=='1':
            return 1 if bv else 0
        else:
            return 0 if bv else 1
    else:
                        
        ans=0        
        for i in range(1,len(s),2):
            if bv: # true
                if s[i] == '&':
                    ans += f_iter(s[:i],True)*f_iter(s[i+1:],True)
                elif s[i] == '|':
                    ans += f_iter(s[:i],True)*f_iter(s[i+1:],False)
                    ans += f_iter(s[:i],False)*f_iter(s[i+1:],True)
                    ans += f_iter(s[:i],True)*f_iter(s[i+1:],True)
                elif s[i] == '^':
                    ans  = f_iter(s[:i],True)*f_iter(s[i+1:],False)
                    ans += f_iter(s[:i],False)*f_iter(s[i+1:],True)                    
            else: # false
                if s[i] == '&':
                    ans += f_iter(s[:i],False)*f_iter(s[i+1:],False)
                    ans += f_iter(s[:i],False)*f_iter(s[i+1:],True)
                    ans += f_iter(s[:i],True)*f_iter(s[i+1:],False)
                elif s[i] == '|':
                    ans += f_iter(s[:i],False)*f_iter(s[i+1:],False)                    
                elif s[i] == '^':
                    ans += f_iter(s[:i],True)*f_iter(s[i+1:],True)
                    ans += f_iter(s[:i],False)*f_iter(s[i+1:],False)
        
        return int(ans%(1e9+7))

#逻辑组合数:动态规划
def f_dynamic_program(s:list,bv:bool)->int:
    """Function: 产生特定逻辑值的逻辑串的计算优先级的组合数:动态规划.

    Args: 逻辑组合数:LR范围搜索
        -s  逻辑串
        -bv 逻辑表达式的值：布尔值,True,False        

    Returns:
        int - 组合数
    """
    if len(s)==0:
        return 0

    T=[]
    F=[]
    for i in range(0,len(s)):
        T.append([0]*len(s))
        F.append([0]*len(s))        
        
    for i in range(len(s)-1,-1,-2):
        for j in range(i,len(s),2):
            if(i%2==1) or (j%2==1):
                continue
            if i==j:               
                if s[i]=='1':
                    T[i][j]=1
                    F[i][j]=0
                if s[i]=='0':
                    F[i][j]=1
                    T[i][j]=0
            else:                    
                for k in range(i,j,2): 
                    if s[k+1] == '&':
                        T[i][j]  += T[i][k]*T[k+2][j]
                        F[i][j]  += F[i][k]*F[k+2][j]
                        F[i][j]  += F[i][k]*T[k+2][j]
                        F[i][j]  += T[i][k]*F[k+2][j]
                    elif s[k+1] == '|':
                        T[i][j]  += T[i][k]*T[k+2][j]
                        T[i][j]  += T[i][k]*F[k+2][j]
                        T[i][j]  += F[i][k]*T[k+2][j]
                        F[i][j]  += F[i][k]*F[k+2][j]
                    elif s[k+1] == '^':
                        T[i][j]  += T[i][k]*F[k+2][j]
                        T[i][j]  += F[i][k]*T[k+2][j]
                        F[i][j]  += F[i][k]*F[k+2][j]
                        F[i][j]  += T[i][k]*T[k+2][j]

                    T[i][j]=int(T[i][j]%1000000007)
                    F[i][j]=int(F[i][j]%1000000007)
    if bv:
        return T[0][len(s)-1]
    else:
        return F[0][len(s)-1]  

'''
s=input()
bv=input()
bv=True if bv=='true' else False
'''
s='0^0^1&0&1&0|0&0|1&0^0&1^0&1|0|0&0|0|1|1^0|1|1&0^1^0|0&1&1&1&0^0^1|1|1^0|1|0^0^0|1|1^0|1^0|0|1^0|0&0^1^0^0|1|0&1|1^1^1&0&0&0|0^1&0^1^1&1&0^0^1|1&0|0^1&1|0|1&0|1&0|0&1^1&0|1|1|0&1&0&0&0|0^0^1&0^0^0^0&1|1^1&1^1|0&0&1&1&1&1&1^1|0|1&1^0^0|1|0|0^1^1&0^0^0|0^1|0|1^0|1|0^1&0&1^1&1^1|1^0|1&0^0|1&0^1|0^1^0&1^0&0|0|0&0|0^1&1|0&1^1&0&0&1&0&0^1&0|0^0|0^1^0&0|0^1&1&0|0^0|0^1^0|0|1^0&1&0^1|1^1^1|1&1^1^0&0^0|1&0|0|0&0&0&1^0|1|1^1&1&0^1^1^1^0&0|0^0|0|0^0|0|1^1^0&1|1&1|0^1|1^0^1|1^0^1|1|1&0&1&1|1^0^0&1&1^0|1&1^0'
bv=True
if is_valid(s)==False:
    print(0)
#print('iter: ',f_iter(s,bv))
#ans=f_iter(s,bv)
ans = f_dynamic_program(s,bv)
print('dynamic: ans%(1e9+7): ',ans,' % ',1e9+7, ' = ',int(ans%(1e9+7)),' ==? ',666719894)