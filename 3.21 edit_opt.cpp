/*  ic--5, dc--3, rc--2
    1)  "abc"    2) "abcfddgdgfdgfghhkkk3454589mcvzvcffgjhkjlsdsffhf";
        "abcd"      "string s2="abcdgdgfdgfddfghhkkk34545.mcvzvcffgjhkjlsdsffhf";

    edit_opt_2d():  14.5us 80.2       185
    edit_opt_1d():   5.5us 112.2      251
*/
#include <windows.h>
#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

// string edit
int edit_opt_2d(string ss,string sd,int p[3])
{   
    //p[0] - insert, p[1] - delete, p[2] - replace    
    int m=ss.length()+1;
    int n=sd.length()+1;

    // int d[m][n];
    int** d = new int*[m];
    d[0] = new int[m*n];
    for(int i = 1; i < m; i++)
        d[i] = d[i-1]+n;

    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(i==0)
            {
                d[i][j]=j*p[0];
                continue;
            }

            if(j==0)
            {
                d[i][j]=i*p[1];
                continue;
            }

            int a=d[i][j-1]+p[0];
            int b=d[i-1][j]+p[1];
            int c=(ss[i-1]==sd[j-1])?(d[i-1][j-1]):(d[i-1][j-1]+p[2]);
            
            d[i][j]=min(a,min(b,c));
        }
    }
    int f=d[m-1][n-1];
    delete d[0];
    delete []d;

    return f;
}

//代价矩阵:  存储结构优化:2D-->1D
//   2D:                                      dp[i-1][j] dp[i-1][j+1] ...  dp[i-1][n]
//           dp[i][j]  dp[i][j] ... dp[i][j]   
//   1D:        dp[0]     dp[1] ... dp[j-1]        dp[j]      dp[j+1] ...       dp[n]
//   tmp:    dp[j] <-- dp[i-1][j],  dp[j] <-- dp[i][j]   //update dp[j]

int edit_opt_1d(string s1,string s2,int p[3])
{
    vector<int> dp(s2.size()+1,0);//???  0
    int minCost = INT_MAX;
    int tmp;
    
    for(int i = 0 ; i <= s2.size() ; i ++){
        dp[i] = i * p[0];
    }
    for(int i = 1 ; i <= s1.size() ; i ++){
        dp[0] = p[1] * i;
        tmp = p[1] * (i-1);
        for(int j = 1 ; j <= s2.size() ; j ++){
            /*minCost = INT_MAX;
            minCost = min(minCost,dp[j] + p[1]);
            minCost = min(minCost,dp[j-1] + p[0]);*/
            minCost = min(dp[j] + p[1],  //delete
                          dp[j-1] + p[0]);//insert
                        
            if(s1[i-1] == s2[j-1]){
                minCost = min(minCost,tmp);// 相同，无需replace，继承上一个状态
            }
            else{
                minCost = min(minCost,tmp+p[2]);//replace
            }
            tmp = dp[j];//上一行的dp[i-1][j]
            dp[j] = minCost;//当前行的dp[i][j]
        }
    }
    
    return dp[s2.size()];
}

int main()
{
    string s1="abcfddgdgfdgfghhkkk3454589mcvzvcffgjhkjlsdsffhfabcfddgdgfdgfghhkkk3454589mcvzvcffgjhkjlsds";
    string s2="abcdgdgfdgfddfghhkkk34545.mcvzvcffgjhkjlsdsffhfcdgdgfdgfddfghhkkk34545.mcvzvcffgjhkjlsdsffhf";
    int p[3]={5,3,2};
    LARGE_INTEGER t1,t2,tc;
    int c;
    float f1,f2,d1=0,d2=0;

    QueryPerformanceFrequency(&tc);

    for(int i=0;i<100;i++)
    {
        QueryPerformanceCounter(&t1);
        c=edit_opt_2d(s1,s2,p);
        QueryPerformanceCounter(&t2);
        f1=(t2.QuadPart-t1.QuadPart)*1000000.0/(float)tc.QuadPart;
        cout<<i<<") "<<f1<<" "<<c;
        QueryPerformanceCounter(&t1);
        c=edit_opt_1d(s1,s2,p);
        QueryPerformanceCounter(&t2);
        f2=(t2.QuadPart-t1.QuadPart)*1000000.0/(float)tc.QuadPart;
        cout<<" "<<f2<<" "<<c<<" ";
        if((i+1)%4==0) cout<<endl;
        d1+=f1;
        d2+=f2;
    }

    cout << s1 <<" --> "<<s2<<":  2D: "<<d1/100.0<<" us"<<":  1D: "<<d2/100.0<<" us"<<endl;
    
    system("pause");

    return 0;
}