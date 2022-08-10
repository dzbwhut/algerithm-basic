#from numpy import array_str

class Node:    
    def __init__(self,paths,ves):  
        self.paths=paths   #边的集合
        self.ves  =ves     #边末端的节点id

    def addPath(self,path,nodeId):
        self.paths.append(path)
        self.ves.append(nodeId)
    
    def searchPath(self, path):
        bExist,idNode=False,-1
        for i in range(len(self.paths)):
            if path==self.paths[i]:
                idNode=self.ves[i]
                bExist=True
                break 

        if bExist==False and len(self.ves)>0:
            idNode=self.ves[0]

        return [bExist,idNode]

class PrefixTree:
    def __init__(self,ds=[]):
        self.nodes=[Node([],[])]
        self.header=self.nodes[0]
        
        if ds!=[]:
            self.generate_dir_tree(ds)

    #添加节点
    def add_node(self, pNode, path, bEnd=0):    
        [bExist,idNode]=pNode.searchPath(path)    
        if bExist:#如果路径已经存在            
            node=self.nodes[idNode]                        
            return node
        else:#
            sz=len(self.nodes)
            node=Node([],[])
            self.nodes.append(node)
            pNode.addPath(path,sz)               
            return node

    def add_branch(self, pNode, fs):        
        for lev in range(len(fs)):             
                #bEnd= 0 if lev<(len(fs)-1) else 1           
                #pNode=self.add_node(pNode,int(fs[lev]),bEnd)
                pNode=self.add_node(pNode,int(fs[lev]))

    def generate_dir_tree(self,ds):
        for d in ds:
            fs=d #.split("\\")            
            self.add_branch(self.header, fs)
            

    #打印树形目录
    def print_dir_node(self,node,splitChar=' ',nSplit=4): 
        for path in node.paths:
            print(splitChar*nSplit,path) 
            i=node.edges[path]            
            self.print_dir_node(self.nodes[i],splitChar,nSplit+4)

    #打印树形目录
    def print_dir_tree(self,splitChar=' ',nSplit=4):    
        node=self.header           
        for path in node.paths:
            print(path) 
            i=node.edges[path]            
            self.print_dir_node(self.nodes[i],splitChar,nSplit)

def generate_mask(nBit):
    mask=0b0
    for i in range(nBit):
        mask<<=1
        mask+=1
    return mask

nBit=32
mask=generate_mask(nBit) 
thr=1<<(nBit-1)
def int2bin(iNum,nBit=32):
    s=bin(iNum) #bin(iNum).replace('0b','') 
    if iNum<0:  
        bumaBin=bin(iNum&mask)  #负数的补码：取绝对值，然后取反，再加1==var&0xffffffff
        s = bumaBin[2:]                       
    else:
        signBit='0'             
        valStr= bin(iNum)[2:]         
        zerosStr= '0'*(nBit-1-len(valStr))
        s = signBit + zerosStr + valStr
    return s

def arr2bin(arr,nBit=32):
    return [int2bin(e,nBit) for e in  arr]   

def xor_prefixTree(s,pT):#补码？？
    node=pT.header    
    v=0   
    for j in range(len(s)):
        v<<=1
        if j==0:   e = int(s[0]) #符号位,优先选同号路径             
        else:    e = 1 if s[j]=='0' else 0
        
        [bExist,idNode]=node.searchPath(e)
        if bExist:#不存在路径            
            bv=e if j==0 else 1 
            v+=bv
        
        node=pT.nodes[idNode] 

    if v>=thr:#负数求原码：
        v-=1
        v=v^mask        
        v=-v
    return  v

def array_xor_max(arr,nBit=32):       
    pT=PrefixTree() 
    d=0
    ds=''
    max_v=0
    xor_v=0
    for i in range(len(arr)):
        if i==0: 
            d=arr[i]     
            ds=int2bin(d,nBit)                
        else: 
            d=arr[i]^d 
            ds=int2bin(d,nBit)   
            if(i<2) :
                max_v=d 
            else:
                xor_v=xor_prefixTree(ds,pT)   
                if xor_v>max_v:
                    max_v=xor_v   

        #print(i,") ",d,ds,xor_v,max_v)

        pT.add_branch(pT.header, ds)
        
    return max_v
  

def xor(s,t):#补码？？  
    v=0
    j=0
    for i in range(len(s)):
        v<<=1
        e = 0 if s[i]==t[i] else 1
        v+=e
         

    if v>=0b100:#负数求原码：
        v-=1
        v=v^0b111     
        v=-v
    return  v

def test_xor():
    a=['111','110','101',   '111','110','101']# -1,-2,-3,  -1,-2,-3
    b=['001','010','011',   '101','111','110']#  1, 2, 3,  -3,-1,-2
    c=[-1,-2,-3,  -1,-2,-3] 
    d=[ 1, 2, 3,  -3,-1,-2]
    for i in range(len(a)):
        print(a[i],' ^ ',b[i],' = ',xor(a[i],b[i]),'  <---- > ',c[i],'^',d[i]," = ",c[i]^d[i])

if '__main__' == __name__:
    #arr=[3,-28,-29,2]
    #arr=list(map(int,input().split()))
    #print(arr,array_xor_max(arr))
    filename='4.15_data.txt'
    mode='r'
    fd=open(filename, mode)
    n=int((fd.readline()).strip())
    arr=[]
    for line in fd:        
        arr.append(int(line.strip()))
    print(array_xor_max(arr))
   
    #test_xor()
    
   