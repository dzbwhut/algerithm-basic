#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <windows.h>

using namespace std;

typedef struct SearchTreeNode
{
    int v;
    int lc;
    int rc;
} STREE_NODE;

typedef struct STreeNodeNumMax
{
    int n;
    int isSTr;
    int min;
    int max;
} STREE_NODE_NUM;

bool cmpTreeNode(STREE_NODE a, STREE_NODE b)
{
    return a.v < b.v;
}

STREE_NODE_NUM maxSearchTree(STREE_NODE *T, int r)
{
    STREE_NODE_NUM stnLf, stnRt, stnRet;

    if (T[r].lc == 0)
        stnLf = {0, 1, T[r].v, T[r].v};
    else
        stnLf = maxSearchTree(T, T[r].lc);

    if (T[r].rc == 0)
        stnRt = {0, 1, T[r].v, T[r].v};
    else
        stnRt = maxSearchTree(T, T[r].rc);

    if (T[r].lc == 0 && T[r].rc == 0)
        stnRet = {1, 1, T[r].v, T[r].v};
    else if (stnLf.isSTr == 1 && stnRt.isSTr == 1 && stnLf.max <= T[r].v &&
             (T[r].v <= stnRt.min || T[r].rc == 0))
        stnRet = {stnLf.n + stnRt.n + 1, 1, stnLf.min, stnRt.max};
    else
        stnRet = {max(stnLf.n, stnRt.n), 0, -1, -1};

    return stnRet;
}

vector<string> split(const string &str, const string &pattern)
{
    // const char* convert to char*
    char *strc = new char[strlen(str.c_str()) + 1];
    strcpy(strc, str.c_str());
    vector<string> resultVec;
    char *tmpStr = strtok(strc, pattern.c_str());
    while (tmpStr != NULL)
    {
        resultVec.push_back(string(tmpStr));
        tmpStr = strtok(NULL, pattern.c_str());
    }

    delete[] strc;

    return resultVec;
}

string input = R"(0 38 30
30 15 27
15 0 34
34 20 28
20 11 0
11 1 0
1 0 0
28 8 35
8 5 3
5 6 18
6 16 0
16 0 0
18 0 0
3 0 0
35 38 0
38 13 0
13 4 2
4 0 0
2 0 0
27 26 25
26 32 22
32 0 0
22 0 21
21 23 0
23 0 0
25 0 19
19 0 9
9 0 17
17 37 12
37 0 33
33 0 36
36 10 0
10 29 31
29 0 0
31 0 7
7 0 0
12 0 24
24 14 0
14 0 0)";

int main()
{
    int n, root;
    STREE_NODE *T;
    STREE_NODE_NUM rev;
    /*
    scanf_s("%d%d", &n, &root);
    T = (STREE_NODE *)malloc(sizeof(STREE_NODE)*(n + 1));
    for (int i = 1; i <= n; i++)
    {
        scanf_s("%d%d%d", &(T[i].v), &(T[i].lc), &(T[i].rc));
    }*/
    
    vector<STREE_NODE> TV;
    vector<string> TS = split(input, "\n");
    vector<string> NS = split(TS[0], " ");
    n = atoi(NS[1].c_str());
    root = atoi(NS[2].c_str());
    T = (STREE_NODE *)malloc(sizeof(STREE_NODE) * (n + 1));
    T[0] = {0, n, root};
    TV.push_back(T[0]);
    for (int i = 1; i <= n; i++)
    {
        NS = split(TS[i], " ");
        T[i] = {atoi(NS[0].c_str()), atoi(NS[1].c_str()), atoi(NS[2].c_str())};
        TV.push_back(T[i]);
    }
    sort(T, T + n + 1, cmpTreeNode);
    // sort(TV.begin(), TV.end(), cmpTreeNode);
    rev = maxSearchTree(T, root);
    cout << rev.n << endl;
    system("pause");

    return 0;
}