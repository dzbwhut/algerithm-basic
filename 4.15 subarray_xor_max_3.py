
class Node:
    def __init__(self):
        self.nexts = [None,None]

class NumTrie:
    def __init__(self):
        self.root = Node()
    
    def add_branch(self, newNum):
        curNode = self.root;
        for move in range(31, -1, -1):
            path = ((newNum >> move) & 1)
            curNode.nexts[path] = Node() if curNode.nexts[path] == None else  curNode.nexts[path]
            curNode = curNode.nexts[path]
        
    def maxXor(self, eori):
        cur = self.root
        res = 0
        for move in range(31, -1, -1):
            path = (eori >> move) & 1        
            best = path if move == 31   else (path ^ 1)
            best = best if cur.nexts[best] != None else (best ^ 1)
            res |= (path ^ best) << move;
            cur = cur.nexts[best]        
        return res    
  
def maxXorSubarray( arr):
    if (arr == None or len(arr) == 0):
        return 0;
    
    max = float('-inf');
    eor = 0    #0..i 异或和
    numTrie = NumTrie()  
    numTrie.add_branch(0)  
    for i in range(0, len(arr)): 
        eor ^= arr[i];
        # X, 0~0 , 0~1, .., 0~i-1
        cur=numTrie.maxXor(eor)
        if cur>0x80000000:
            cur-=1
            cur=cur^0xFFFFFFFF        
            cur=-cur
        max = cur if cur>max else max
        numTrie.add_branch(eor)
     
    return max;
 

if '__main__' == __name__:
    '''n = int(input())
    arr = list(map(int, input().split()))
    print(maxXorSubarray(arr))  # 输出最大异或和
    '''
    filename='4.15_data.txt'
    mode='r'
    fd=open(filename, mode)
    n=int((fd.readline()).strip())
    arr=[]
    for line in fd:        
        arr.append(int(line.strip()))
        
    #arr=[3,-28,-29,2]
    print(maxXorSubarray(arr))