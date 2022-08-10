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
    
