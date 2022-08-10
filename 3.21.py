import numpy as np
'''
str1=input()
str2=input()
cs=input().split()
cs=[int(e) for e in cs]
string s1="abcd2";//"abcfddgdgfdgfghhkkk3";//"abcfddgdgfdgfghhkkk3454589mcvzvcffgjhkjlsdsffhf";
    string s2="aecrd";//"abcdgdgfdgfddfghhkkk345";//"45.mcvzvcffgjhkjlsdsffhf";
'''
s1=['a','bcd','efg1','hij','klmno', 'pqrstekeelmno','uvwxyz8', "abcd2"]
s2=['ab','bd','efg2','hij','elmn1o','pqrsteeeklmno','12uvwxyz',"aecrd"]
cs=[5,3,2] # insert 5, delete 3, replace 2
cs_max=sum(cs)*5

print("\n----------- str1-->str2:   insert 5, delete 3, replace 2----------\n")
for i in range(len(s1)):
    str1,str2=s1[i],s2[i]
    m,n=len(str1)+1,len(str2)+1

    # init dp[m+1][n+1]
    dp = np.zeros([m,n])  # dp[i][j] means the min edit distance between str1[:i] and str2[:j]
    ops=[]
    for i in range(m):    
        for j in range(n):        
            if i==0:
                dp[i][j]=j*cs[0]
                continue   

            if j==0:
                dp[i][j]=i*cs[1]
                continue  

           
            # insert: xy --> xzy
            '''if str1[i]==str2[j-1]:
                print(str1[:i+1],"->", str2[:j+1], " insert: ", cs[0])                
                a=dp[i][j-1]+cs[0]
            '''
            #print(str1[:i+1],"->", str2[:j+1],'\n')            
            a=dp[i][j-1]+cs[0]
            #print("     insert: ", a)

                
            # delete
            '''if str1[i-1]==str2[j]:
                print(str1[:i+1],"->", str2[:j+1], " delete: ", cs[1])
                b=dp[i-1][j]+cs[1]'''
            b=dp[i-1][j]+cs[1]            
            #print("     delete: ", b)
                
            # replace
            '''if str1[i-1]==str2[j-1]:  
                if str1[i]==str2[j]:
                    print(str1[:i+1],"->", str2[:j+1], " No replace: ",0)
                    c=dp[i-1][j-1]    
                else:   
                    print(str1[:i+1],"->",str2[:j+1], " replace: ",cs[2])
                    c=dp[i-1][j-1]+cs[2]'''
            c = dp[i-1][j-1] if str1[i-1]==str2[j-1] else dp[i-1][j-1]+cs[2]             
            #print("     replace: ", c)   

            dp[i][j] = min([a,b,c]) 
            #print("        ==> select: ",dp[i][j],"\n\n")        
            '''if cs_max!=cs_min: 
                print("        ==> select: ",cs_min,"\n")
                dp[i][j]=cs_min  # select the min edit distance''' 
                
            #ops.append(('insert','delete','replace')[[a,b,c].index(dp[i][j])])     
                
    print("\n* opt:  ", str1," -> ",str2,": ",dp[m-1][n-1], '\n', dp,"\n\n")

print("\n==========================  End  ======================\n")