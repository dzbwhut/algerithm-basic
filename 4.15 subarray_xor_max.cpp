#include <iostream>

using namespace std;

// 前缀树的节点类型，每个节点向下只可能有走向0或1的路
typedef struct Node {
    struct Node *nexts[2]={NULL,NULL};
}NODE;

// 基于本题，定制前缀树的实现
class NumTrie {
    public:
    // 头节点
    NODE *head=new NODE();

    // 把某个数字newNum加入到这棵前缀树里
    // num是一个32位的整数，所以加入的过程一共走32步
    void add(int newNum) {
        NODE *cur = head;
        for (int move = 31; move >= 0; move--) {
            int path = ((newNum >> move) & 1);            
            cur->nexts[path] = cur->nexts[path] == NULL ? new Node()
                    : cur->nexts[path];
            cur = cur->nexts[path];
        }
    }

    // 给定一个eorj，eorj表示eor[j]，即以j位置结尾的情况下，arr[0..j]的异或和
    // 因为之前把eor[0]、eor[1]...eor[j-1]都加入过这棵前缀树，所以可以选择出一条最优路径来
    // maxXor方法就是把最优路径找到，并且返回eor[j]与最优路径结合之后得到的最大异或和
    int maxXor(int eori) {
        Node *cur = head;
        int res = 0;
        for (int move = 31; move >= 0; move--) {
            int path = (eori >> move) & 1;
            int best = move == 31 ? path : (path ^ 1);
            best = cur->nexts[best] != NULL ? best : (best ^ 1);
            res |= (path ^ best) << move;
            cur = cur->nexts[best];
        }
        return res;
    }
};

 int maxXorSubarray(int arr[], int n) {
    if (arr == NULL || n == 0) {
        return 0;
    }
    int max = INT_MIN;
    int eor = 0; // 0..i 异或和
    NumTrie numTrie = NumTrie();
    numTrie.add(0);
    for (int i = 0; i < n; i++) {
        eor ^= arr[i];
        // X, 0~0 , 0~1, .., 0~i-1
        int val = numTrie.maxXor(eor);
        if(max < val)  max = val;       
        numTrie.add(eor);
    }
    return max;
}

int main() {
    /*int n;
    cin >> n;

    int[] arr = new int[n];
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }*/
    int arr[4] ={3,-28,-29,2};
    cout<<maxXorSubarray(arr,4)<<endl;
}

