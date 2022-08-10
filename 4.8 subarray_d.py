
max_bi_que=[]
mv_L=1
mv_R=2

#解1:遍历分割，求左，右最大值，求左右差的绝对值的最大值
#解1.1 求最大值:   用双向队列，每次插入一个元素，每次删除一个元素，求最大值，整体max的平均复杂度为O(1)
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
    
#解1.2 求左右差的绝对值的最大值
def sub_array_max_d(arr):
    """
    Given an array of integers, find the maximum values.
    """
   
    mx=[0]*n
    for i in range(n):
        mx[i]=array_max_biQue(arr,0,i,mv_R)

    mx_v=0
    for i in range(n):
        rv=array_max_biQue(arr,i,n-1,mv_L)
        di=abs(mx[i]-rv)
        if di>mx_v:
            mx_v=di
    return mx_v

#解2: 总体最值与两端值 max(arr)-min(arr[0],arr[-1]) 
def sub_array_max_d_2(arr):
    mx_v=arr[0]
    for i in range(1,n):
        if mx_v<arr[i]:
            mx_v=arr[i]
    return mx_v-min(arr[0],arr[-1])

#解3  总体最值与两端值 max(arr)-min(arr[0],arr[-1])
def sub_array_max_d_3(arr):
    return max(arr)-min(arr[0],arr[-1])


if '__main__'==__name__:
    #n=int(input())
    #arr=list(map(int,input().split()))
    n=5
    arr=[3,5,1,4,2]
    
    print(sub_array_max_d(arr))
    print(sub_array_max_d_2(arr))
    print(sub_array_max_d_3(arr))