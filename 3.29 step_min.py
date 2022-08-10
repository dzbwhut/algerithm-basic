
def gcd(n):
    cd=[]
    for i in range(2,int(n**.5)+2):
        if n%i==0 :
            if i not in cd:
                cd.append(i) 
            k=n//i
            if k not in cd:
                cd.append(k)
    return cd

def step_min(n,m,c,s=-1,z=-1):    
    if n>m:
        return -1
    elif n==m  or (z !=-1 and s>=z):
        print(n,s)   
        return s

    if(len(c[n])==0):
        c[n]=gcd(n)
        #c降序排列
        c[n].sort(reverse=True)  

    k=len(c[n])
    if k==0:
        return -1
    print(n,s,c[n])   
    
    for i in range(k):        
        t=step_min(n+c[n][i],m,c,s+1,z)
        if t>-1 and (z==-1 or t<z):
            z=t   
            break            
    return t 

lst=[]

def step_min_infer(n,m,c,s=0,z=-1):    
    
    if(len(c[n])==0):
        c[n]=gcd(n)
        #c降序排列
        c[n].sort(reverse=True)  

    k=len(c[n])
    if k==0:
        return -1
    # print(n,s,c[n])   

    t=-1
    for i in range(k):
        if  z !=-1 and (s+1>=z): 
            t=-1
            break 
        ni=n+c[n][i]  
        if i==0 and len(lst)==s:
            lst.append(c[n][i])
        else:
            lst[s]=c[n][i] 
            while len(lst)>s+1: 
                lst.pop()        

        #print("\t ",s+1," - ",i, " - ",n,"  ",c[n][i],"---->",ni,t) 
        if ni>m:  t=-1 
        elif ni==m: 
            t = s+1  #本层不必探索了   
            print("\t ***** ",t," *****",lst)
        else: 
            st='    '*s
            print(st,s+1," - ",i, " - ",n,"  ",c[n][i],"---->",ni,t) 
            t,z=step_min_infer(ni,m,c,s+1,z)
        
        if (z==-1 and t!=-1) or (t>0 and t<z): 
            z=t
            t=-1
        if  z !=-1 and t>=z:
            break
            
    return t,z 
#s=input().split()
#n,m=int(s[0]),int(s[1])
n,m,v=  4,16,10  #8,678,31 #  4,24,5#    676,12948,10
c=[[]]*(m+1)
#print(step_min(n,m,c)+1)
t,z=step_min_infer(n,m,c)
print(z)