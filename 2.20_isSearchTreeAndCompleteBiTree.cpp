#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>
#include <windows.h>

using namespace std;

string input = R"(0 49 47
47 30 21
30 14 11
14 26 3
26 16 37
16 36 7
36 0 0
7 0 0
37 1 27
1 0 0
27 0 0
3 8 39
8 48 33
48 0 0
33 0 0
39 19 44
19 0 0
44 0 0
11 40 35
40 13 15
13 29 6
29 0 0
6 0 0
15 42 5
42 0 0
5 0 0
35 31 25
31 41 38
41 0 0
38 0 0
25 17 18
17 0 0
18 0 0
21 45 4
45 34 2
34 22 46
22 20 49
20 0 0
49 0 0
46 0 0
2 10 28
10 0 0
28 0 0
4 23 24
23 12 9
12 0 0
9 0 0
24 32 43
32 0 0
43 0 0)";

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

typedef struct CBTree
{
    int deep;
    int NodeNum;
    bool isCBT;
} CBTREE_ST;

bool cmpTreeNode(STREE_NODE a, STREE_NODE b)
{
    return a.v < b.v;
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

int deep(STREE_NODE *T, int r)
{
    return 0;
}

CBTREE_ST isCompleteBinaryTree(STREE_NODE *T, int r)
{
    CBTREE_ST Rev, RevLf, RevRt;

    if (T[0].lc == 0 || T[0].lc == 0)
        return Rev = {0, 0, false};

    if (T[r].lc == 0 && T[r].rc == 0)
        return Rev = {1, 1, true};

    if (T[r].lc == 0)
        RevLf = {0, 0, true};
    else
        RevLf = isCompleteBinaryTree(T, T[r].lc);

    if (T[r].rc == 0)
        RevRt = {0, 0, true};
    else
        RevRt = isCompleteBinaryTree(T, T[r].rc);

    if (RevLf.isCBT == false || RevRt.isCBT == false ||
        RevLf.deep > RevRt.deep + 1 || RevLf.deep < RevRt.deep)
        return Rev = {-1, -1, false};

    if (RevLf.deep == RevRt.deep) //左子树深度应等于右子树深度，
    {
        if (RevLf.NodeNum != ((1 << RevLf.deep) - 1))
            return Rev = {-1, -1, false};

        if (RevRt.NodeNum < ((1 << (RevRt.deep - 1)) - 1))
            return Rev = {-1, -1, false};

        Rev.isCBT = true;
        Rev.NodeNum = RevLf.NodeNum + RevRt.NodeNum + 1;
        Rev.deep = RevLf.deep + 1;

        return Rev;
    }
    else if (RevLf.deep == RevRt.deep + 1)
    { //

        if (RevRt.NodeNum != ((1 << RevRt.deep) - 1))
            return Rev = {-1, -1, false};

        if (RevLf.NodeNum < ((1 << (RevLf.deep - 1)) - 1))
            return Rev = {-1, -1, false};

        Rev.isCBT = true;
        Rev.NodeNum = RevLf.NodeNum + RevRt.NodeNum + 1;
        Rev.deep = RevLf.deep + 1;

        return Rev;
    }

    return Rev = {-1, -1, false};
}

int main()
{
    int n, root;
    STREE_NODE *T;
    STREE_NODE_NUM rev;
    /*
    scanf("%d%d", &n, &root);
    T = (STREE_NODE *)malloc(sizeof(STREE_NODE) * (n + 1));
    T[0] = {0, n, root};
    for (int i = 1; i <= n; i++)
    {
        scanf("%d%d%d", &(T[i].v), &(T[i].lc), &(T[i].rc));
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

    sort(T + 1, T + n + 1, cmpTreeNode);

    rev = maxSearchTree(T, root);
    string isST = rev.isSTr == 1 ? "true" : "false";

    CBTree revCBT = isCompleteBinaryTree(T, root);
    string isCBT = revCBT.isCBT == true ? "true" : "false";

    cout << isST << endl
         << isCBT << endl;
}