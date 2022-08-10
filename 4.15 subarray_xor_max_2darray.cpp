#include <cstdio>
#include <cstring>
#include <algorithm>
 
using namespace std;
 
const int N = 100000;
const int M = N * 32 + 1;
 
int trie[M][2], idx;
 
void add( int x ) {
    int p = 0;   // root of the trie
    for ( int i = 31; i >= 0; --i) {
        int u = x >> i & 1;     // 取位权
        int &t = trie[p][u];    // 子节点引用, u--位权，也是路径下标
        if ( !t ) t = ++idx;    // 如果子节点为空，则创建子节点, 并设置为idx,引用值与原变量共享存储，变则同变
        p = t;                  // 深度遍历，子节点id更新
    }
}
 
int query( int x ) {
    int ret = 0, p = 0;
    int u = x >> 31 & 1;//符号位处理
    if ( !trie[p][u] ) {//符号位：[0]--正数路径不存在，[1]--负数路径不存在
        ret |= 1 << 31; //符号位：bit[31]--1 负数
        u ^= 1;         //向异号分支探索：bit[31]--0 正数
    }
    p = trie[p][u];     //深度遍历，更新p
    for ( int i = 30; i >= 0; --i ) {//从高到低，深度遍历值域位权重，更新ret
        u = x >> i & 1;  //域位权重
        int &t = trie[p][u ^ 1];//异号分支
        if ( t ) {//异号存在
            ret |= 1 << i;//本位异或==1
            p = t;       //深度遍历，更新p
        } else p = trie[p][u];//异号不存在，本位异或==0，更新p
    }
    return ret;
}
 
int main(void) {
    int n, x;
    int ret = 0, eor = 0;
    scanf("%d", &n);
    while ( n-- ) {
        scanf("%d", &x);
        eor ^= x;
        ret = max( ret, query(eor) );
        add( eor );
    }
    printf("%d\n", ret);
    return 0;
}