
min_bi_que=[]
max_bi_que=[]
mv_L=1
mv_R=2
#mv_LR=3

def array_min_biQue(arr, L, R, mode=mv_R):
    """
    Given an array of integers, find the minimum values.
    """

    global min_bi_que,mv_L,mv_R
    #L->
    if mode==mv_L:  
        while len(min_bi_que)>0:  
            if L>min_bi_que[0]:
                min_bi_que.pop(0)
            else:
                break
    #R->  
    else:    
        while True:
            if len(min_bi_que)==0  or arr[min_bi_que[-1]]<arr[R]: #升序
                min_bi_que.append(R)
                break
            else:
                min_bi_que.pop()
             
    return arr[min_bi_que[0]]


def array_max_biQue(arr, L, R, mode=mv_R):
    """
    Given an array of integers, find the maximum values.
    """
    global max_bi_que,mv_L,mv_R

    #L->
    if mode==mv_L:        
        while len(max_bi_que)>0:  
            if L>max_bi_que[0]:
                max_bi_que.pop(0)
            else:
                break
    else:           
        #R->    
        while True:
            if len(max_bi_que)==0  or arr[R]<arr[max_bi_que[-1]]: #降序
                max_bi_que.append(R)
                break
            else:
                max_bi_que.pop()
             
    return arr[max_bi_que[0]]
    

def array_min(arr, L, R, reset=False):
    """
    Given an array of integers, find the minimum and maximum values.
    """

    min_val = arr[L]    
    for i in range(L,R+1):
        if arr[i] < min_val:
            min_val = arr[i]        
    return  min_val

def array_max(arr, L, R, mode):
    """
    Given an array of integers, find the minimum and maximum values.
    """

    max_val = arr[L]
    for i in range(L,R+1):       
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def sub_array_num(arr,num):
    """
    Given an array of integers, find the number of sub-arrays that have a sum of zero.
    """
    count = 0
    L,R=0,0
    
    
    mode=mv_R
    while R<len(arr) and L<=R:         
        maxV=array_max_biQue(arr,L,R,mode) #
        minV=array_min_biQue(arr,L,R,mode)  # 
        if maxV-minV<=num and R+1<len(arr):
                R+=1   
                mode=mv_R                                          
                continue  
        else:
            count+=R-L
            if maxV-minV<=num:
                count+=1
            #print(count)
            if L<R:
                L+=1 
                mode=mv_L 
            elif R+1<len(arr):
                R+=1
                mode=mv_R 
            else:
                break

    global max_bi_que
    max_bi_que=[]       
    global min_bi_que
    min_bi_que=[]       

    return count


if __name__ == '__main__':
    #s=input().split()
    #[n,num]=list(map(int,s))
    #s=input().split()
    #arr=list(map(int,s))
    #arr=[int(x) for x in input().split()]
    arr=[[1,2,3,4,5],[3,6,7,4,8,5,2,6,1]]
    num=[2,4]
    for i in range(len(num)):
        print(arr[i],"   ",num[i],"   ",sub_array_num(arr[i],num[i]))
        
    

