

class Node:    
    def __init__(self, id=0, iPass=0, bEnd=0, edges={}):        
        self.id=id
        self.iPass=iPass # passed-counter
        self.bEnd=bEnd
        self.paths=[] #['a', 'b', 'c'] 
        self.edges=edges #{'a':1, 'b':2, 'c':3}  'a' is path, 1 is 末端节点ID
    
class PrefixTree:
    def __init__(self,ds=[]):
        self.nodes=[Node(0,0,0,{})]
        self.header=self.nodes[0]
        
        if ds!=[]:
            self.generate_dir_tree(ds)

    #添加节点
    def add_node(self, pNode, path, bEnd):        
        if path in pNode.paths:#如果路径已经存在
            ni=pNode.edges[path]  
            node=self.nodes[ni]          
            node.iPass+=1
            if bEnd==1: node.bEnd=bEnd            
            return node
        else:#
            sz=len(self.nodes)
            node=Node(sz, 1, bEnd, {})
            self.nodes.append(node)
            pNode.paths.append(path)
            pNode.edges[path]=sz            
            return node

    def generate_dir_tree(self,ds):
        for d in ds:
            fs=d.split("\\")
            pNode=self.header

            for lev in range(len(fs)):             
                bEnd= 0 if lev<(len(fs)-1) else 1           
                pNode=self.add_node(pNode,fs[lev],bEnd)

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

if '__main__' == __name__:
    ds=['a\\b\\c','a\\d\\d','a\\b\e','b\c\\fg']

    pT=PrefixTree(ds)    

    pT.print_dir_tree(splitChar='-',nSplit=4)
    