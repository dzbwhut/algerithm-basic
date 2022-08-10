# 求最长幸运字符串
# 小A很喜欢字母N，他认为连续的N串是他的幸运串。
# 有一天小A看到了一个全部由大写字母组成的字符串，
# 他被允许改变最多2个大写字母（也允许不改变或者只改变1个大写字母），
# 使得字符串中所包含的最长的连续的N串的长度最长。
'''
1 2 3 4 5 6 7 8 9 10 11 12 13
1 1 2 4 3 3 9 6 6  9  5  7 49 37 32 53 45 49 8 8
1 1 2 4 3 2 9 6 4  8  5  7 45 37 32 53 45 49 8 8
          6     9 10

6 NAN
9 NNNNBB
10 NNNNBNNNN
'''
se=["O","ANA","NAN","NNNNBB","NNNNBNNNN"]

def luck_string_max_clear(ds):
    ns=[0] #N串的长度
    ss=[] #间隔串的长度
    k=0 #N串的编号
    j=-1 #间隔串的编号
    
    if len(ds)<1:
        return 0
        
    #确保交叉序列 :  “ns”,ss,ns,ss
    
    if ds[0]=='N':
        ns[k]+=1
    else:  #“ss”开始,增加ns[0]=0
        ss.append(0)   
        j+=1
        ss[j]+=1
        

    #遍历ds串
    for i in range(1,len(ds)):
        if ds[i]=='N':
            if  ds[i-1]!='N':
                ns.append(0)   
                k+=1
            ns[k]+=1    
        else:
            if  ds[i-1]=='N':
                ss.append(0)
                j+=1
            ss[j]+=1
    
    #计算最大长度--遍历ns:  ns初始化为[0]         
    maxN=0  # N串的最大长度
    for i in range(len(ns)):# N串存在
        lr=ns[i]
        if len(ss)>i: #右侧   ss[i]存在："...Nccc"            
            lr += min(2,ss[i]) # NS[i] + SS[i]
            if ss[i]<=2 and len(ns)>i+1: #如果当前N串的间隔串的长度小于等于2，则可以拼接
                lr += ns[i+1]  # NS[i] + 1s/2s + NS[i+1]                 
                if ss[i]==1:# NS[i] 1s NS[i+1]，后续的N串，S串，可以拼接 
                    if len(ss)>i+1: #ss[i+1]存在
                        lr += 1 #NS[i] 1s NS[i+1] 1s
                        if ss[i+1]==1 and len(ns)>i+2: #如果当前N串的间隔串的长度为1，且下一个N串的间隔串的长度为1，则可以拼接
                            lr += ns[i+2] #NS[i] 1s NS[i+1] 1s NS[i+2]
                        # else:  
                        #   NOP     #ss[i+1]>1 不可以拼接；NS[i+2]不存在，无串可拼接  
                    elif i>0: #ss[i+1]不存在，ss[i-1]存在
                        lr += 1 # 1s NS[i] 1s NS[i-1]
                # else:  NS[i] + 2s + NS[i+1]  
                #   NOP     #ss[i]>=2 后续串不再拼接 
            elif ss[i]==1 and i>0: #如果当前N串的间隔串的长度为2，且下一个N串的间隔串的长度为1，则可以拼接
                lr += 1
        elif i>0:#末尾的N串，且非头，右侧不存在ss，左侧存在："...cccN"
            lr += min(2,ss[i-1])    

        maxN=max(maxN,lr)

    if len(ns)==0 and len(ss)>0:#N串不存在，只有间隔串
        maxN=min(2,ss[0])

    return maxN      

# 输出最长幸运字符串，少用存储空间，一次遍历
def luck_string_max_opt(ls):
    #N串的长度：相邻3个N串的长度
    ns=[0,0,0]
    #3个N串的2个间隔距离
    ss=[0,0]

    max = 0 #最大长度
    id_ns=0 #当前N串的编号
    id_ss=0 #当前间隔距离的编号
    #遍历字符串
    for i in range(n):
        length=1
        #计算当前N串的长度
        if s[i] == 'N':
            ns[id_ns] += 1  
            if s[i-1] != 'N': 
                if ss[id_ss]==1:
                    id_ss = (id_ss+1)%2
        else:
            ss[id_ss] += 1
            if s[i-1]=='N':
                if ss[id_ss]==1:
                    id_ss = (id_ss+1)%2  

        #如果当前字符串的长度大于最大长度，则更新最大长度
        if length > max:
            max = length
    return max



#for i in range(10):
#    #从控制台获取字符串
#    s = input()
#    #计算字符串长度
#    n = len(s)
#    print(i,") ",s,luck_string_max_clear(s))
i=0
for s in se:  
    i+=1
    print(i,") ",s,luck_string_max_clear(s))