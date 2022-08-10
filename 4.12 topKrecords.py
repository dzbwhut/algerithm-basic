
def update_heap(hp, map_h, i):    
    #更新小根堆，仅仅调整堆序，不更新堆值
    while i<len(hp)-1:
        if hp[i]>hp[i+1]:#下沉，交换
            hp[i],hp[i+1]=hp[i+1],hp[i]
            map_h[i],map_h[i+1]=map_h[i+1],map_h[i]
        else:
            break
        i+=1
    return 

#堆顶插入元素，并更新小根堆
def push_heap(hp, map_h,key, value):    
    map_h.insert(0,key)
    hp.insert(0,value)
    ln=len(map_h)
    if ln==1:
        return   
                
    update_heap(hp, map_h, 0)

    return

s=[ 'a','d','c','d','f','a','b','b','a','b',
    'b','a','d','b','a','c','b','a','b','b']
n=len(s)
topk=4

hp=[] #小根堆：
map_h=[] #小根堆：堆中的元素

map_r={}#词频记录表
s_r=[]#词汇表:词汇集s去重

for w in s:
    if w not in s_r:
        map_r[w]=1
        s_r.append(w)
    else:   
        map_r[w]+=1

    '''  统计词频同时，更新小根堆，高频词频繁更新
    if w in map_h: #在堆，更新
        i=len(map_h)-1
        #i=find(w,map_h)  #查找w在堆中的位置
        while i>=0 and w !=map_h[i]:  i-=1        
        hp[i]=map_r[w]      
        update_heap(hp, map_h, i)
    elif len(map_h)<topk: #不在堆，堆没满，插入
        push_heap(hp, map_h, w,  map_r[w])        
    elif map_r[w]>hp[0]:#不在堆，且>堆顶，更新
        hp[0]=map_r[w]
        map_h[0]=w
        update_heap(hp, map_h, 0)
    '''

#统计词频后，更新小根堆，每词更新一次
for w in s_r:
    if w in map_h: #在堆，更新
        i=len(map_h)-1
        #i=find(w,map_h)  #查找w在堆中的位置
        while i>=0 and w !=map_h[i]:  i-=1        
        hp[i]=map_r[w]      
        update_heap(hp, map_h, i)
    elif len(map_h)<topk: #不在堆，堆不满，插入
        push_heap(hp, map_h, w,  map_r[w])        
    elif map_r[w]>hp[0]:#不在堆，堆满，且>堆顶，更新
        hp[0]=map_r[w]
        map_h[0]=w
        update_heap(hp, map_h, 0)

print(map_h,hp,map_r)

            