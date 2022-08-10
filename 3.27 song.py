#求最小合唱难度

#求数组的梯度
def grad(arr):
    #求数组的梯度
    g = []
    for i in range(len(arr)-1):
        g.append(abs(arr[i+1]-arr[i]))
    return g


def get_new_g(arr,g,g_id,g_cluster):
    d1 ,d2=0,0
    d=arr[g_id+1]-arr[g_id]
    if d>0:
        for i in range(g_id,-2,-1):
            if i in g_cluster:
                continue
        if i>=0:    
            d1=abs(arr[g_id+2]-arr[i])
            if d1<d:
                g[g_id+2]=d1
                #g_sum=g_sum-(g[g_id+2]-d1)
            else:
                g_cluster.append(g_id+2)   
     
                

    elif d==0:
        if g_id in g_cluster:
            g_cluster.append(g_id+1)
    else:#d<0
        if g_id in  g_cluster:
            return g

    return g_new
    
def update_g(g_id,g_cluster,arr):
    g_cluster.append(g_id)
    g_sum=g_sum-(g[g_id]-g_new)

    if g_id[i]<g_id[i-1]:#左侧
        #更新g_id[i-1]对应的梯度
        if i-1==0:
            g[g_id[i-1]]=0
        else:
            g[g_id[i-1]]=arr[g_id[i]]-arr[g_id[i-1]]

        
    elif g_id[i-1]<g_id[i]:#右侧
        #更新g_id[i]对应的梯度
        g[g_id[i]]=arr[g_id[i+1]]-arr[g_id[i]]

    return g_cluster


#从控制台获取数量
num = int(input("请输入数量："))
#从控制台获取数组
arr = input("请输入数组：").split()
#将数组转换为数字
arr = [int(e) for e in arr]
g=grad(arr)

#求梯度的总和
g_sum=sum(g)

#梯度降序排序
g_sort=sorted(g,reverse=True)#排序稳定性：相同梯度的顺序不变，获取有序梯度的原ID
g_id=[g.index(g_sort[i]) for i in range(len(g))]
#梯度聚类：2类
g_cluster=[g.index(g[0])]#有相同梯度时
g_sum=g_sum-g[g_id[0]]

#扫描梯度
for i in range(1,len(g)):
    #选择大梯度，加入第二类，并更新梯度    
    g_id=g.index(g[i])

    #继续加入第二类的条件：新梯度<原梯度
    g_new=get_new_g(g_id,g_cluster,arr)

    if g_new<g[g_id]:
       update_g(g_id,g_cluster,arr)

g_sum=sum(g) 