#n=int(input())
#arr=input().split()
n=23
arr='24 13 2 4 54 23 12 53 12 23 42 13 53 12 24 12 11 24 42 52 12 32 42'
arr=arr.split()
arr=[int(i) for i in arr]

if n!=len(arr):
    print(0)
    exit()

if n<2:
    print(0)
elif n==2:
    print(abs(arr[1]-arr[0]))
else:
    g_max=0
    g_max_id=0
    for i in range(n-1):
        g=abs(arr[i+1]-arr[i])
        if g>g_max:
            g_max=g
            g_max_id=i

    if g_max==0:
        print(0)
    else:
        g_sum_p=0
        g_cluster1=[]
        g_cluster2=[]
        if arr[g_max_id+1]>arr[g_max_id]:
            g_cluster2.append(arr[g_max_id+1])
            g_cluster1.append(arr[g_max_id])
        else:
            g_cluster2.append(arr[g_max_id])
            g_cluster1.append(arr[g_max_id+1])

        for i in range(g_max_id-1,-1,-1):
            d1=abs(g_cluster1[0]-arr[i])
            d2=abs(g_cluster2[0]-arr[i])
            if d1<d2:
                g_sum_p+=d1
                g_cluster1.insert(0,arr[i])
            else:
                g_sum_p+=d2
                g_cluster2.insert(0,arr[i])

        for i in range(g_max_id+2,n):
            d1=abs(arr[i]-g_cluster1[-1])
            d2=abs(arr[i]-g_cluster2[-1])
            if d1<d2:
                g_sum_p+=d1
                g_cluster1.append(arr[i])
            else:
                g_sum_p+=d2
                g_cluster2.append(arr[i])

        print(g_sum_p)

        g_sum=0
        for i in range(len(g_cluster1)-1):
            g_sum+=abs(g_cluster1[i+1]-g_cluster1[i])
        
        for i in range(len(g_cluster2)-1):
            g_sum+=abs(g_cluster2[i+1]-g_cluster2[i])

        print(arr,":  ",g_sum,"=?=", g_sum_p,"\n    c1: ",g_cluster1,"\n    c2: ",g_cluster2)