#include <iostream>
#include <vector>

using namespace std;
// 局部最优--仅仅比较两类中最近的元素的梯度
int song_min(int n, vector<int> arr,bool debug) 
{
    int g_sum_p=0;
    if(n<3)    g_sum_p=0;    
    else{
        int g_max=0,g_max_id=0,g; 
        
        for(int i=0;i<n-1;i++){            
            g=abs(arr[i+1]-arr[i]);
            if(g>g_max)    g_max=g, g_max_id=i;
        }
         
        if(g_max==0)
            g_sum_p=0;
        else{
            int d1,d2;
            vector <int> g_cluster1;
            vector <int> g_cluster2;
            if(arr[g_max_id+1]>arr[g_max_id])
                g_cluster2.push_back(arr[g_max_id+1]),
                g_cluster1.push_back(arr[g_max_id]);
            else
                g_cluster2.push_back(arr[g_max_id]),
                g_cluster1.push_back(arr[g_max_id+1]);

            for(int i=g_max_id-1;i>=0;i-=1){
                d1=abs(g_cluster1[0]-arr[i]);
                d2=abs(g_cluster2[0]-arr[i]);
                if(d1<d2)  g_sum_p+=d1,   g_cluster1.insert(begin(g_cluster1),arr[i]);
                else       g_sum_p+=d2,   g_cluster2.insert(begin(g_cluster2),arr[i]);
            }

            for(int i=g_max_id+2;i<n;i++){
                d1=abs(arr[i]-g_cluster1[g_cluster1.size()-1]);
                d2=abs(arr[i]-g_cluster2[g_cluster2.size()-1]);
                if(d1<d2) g_sum_p+=d1, g_cluster1.push_back(arr[i]);               
                else      g_sum_p+=d2, g_cluster2.push_back(arr[i]);
                
            }  

            if(debug) {
                cout << "arr: ";
                for(int i=0;i<arr.size();i++)
                    cout<<arr[i]<<" ";
                cout << "\nc1: ";

                for(int i=0;i<g_cluster1.size()-1;i++)
                    cout<<g_cluster1[i]<<" ";            
                cout << "\nc2: ";

                for(int i=0;i<g_cluster2.size();i++)
                cout<<g_cluster2[i]<<" ";
                cout <<":  "<<g_sum_p<<"=?="<<188<<endl;
            }
        }        
    }
    return g_sum_p;
}

//2D备忘录：dp[N][N] + ans[N]  性能: 16ms  14220KB
int zuihe(vector<int> yin){
   if(yin.size() < 3)
      return 0;
   int dp[yin.size()][yin.size()];
   dp[1][0] = 0;
   int ans[yin.size()];
   ans[1] = 0;

   // 长度为i的最小梯度：
   for(int i = 2; i < yin.size(); i++){
      //1 基准：第一类：0~i-1--给Q唱的难度， 第二类：i--仅仅一个音符给牛唱，难度为 0
      ans[i] = ans[i-1] + abs(yin[i-1] - yin[i-2]);
      dp[i][i-1] = ans[i];
      //以j为界，分成左右两类：0~j, j+1~i-1;
      //i分别并入左右部，选最小值  
      for(int j = 0; j < i-1; j++){
        // i-->左部
        dp[i][i-1] = min(dp[i][i-1],dp[i-1][j] + abs(yin[i] - yin[j]));
        // i-->右部
        dp[i][j] = dp[i-1][j] + abs(yin[i] - yin[i-1]);
      }
   }

   // 找出最小的dp[i][i]
   int min_num = dp[yin.size()-1][0];
   for(int j = 1; j < yin.size()-1; j++){
       min_num = min(dp[yin.size()-1][j],min_num);
   }

   return min_num;
}

//2row 备忘录: 仅仅记录上一行和当前行，用下标型指针，交替更新当前行与上一行   
//性能: 9ms 432kB
int zuihe_2row(vector<int> yin){
   if(yin.size() < 3)
      return 0;

   int dp[2][yin.size()];
   dp[0][0] = dp[0][1] = 0;

   int L=0; //上一行ID
   int C=1; //当前行ID
   // 长度为i的最小梯度：
   for(int i = 2; i < yin.size(); i++){
      //1 基准：第一类：0~i-1--给Q唱的难度， 第二类：i--仅仅一个音符给牛唱，难度为 0
      dp[C][i] = dp[L][i-1] + abs(yin[i-1] - yin[i-2]);
      dp[C][i-1] = dp[C][i];
      //以j为界，分成左右两类：0~j, j+1~i-1;
      //i分别并入左右部，选最小值  
      for(int j = 0; j < i-1; j++){
        // i-->左部
        dp[C][i-1] = min(dp[C][i-1], dp[L][j] + abs(yin[i] - yin[j]));
        // i-->右部
        dp[C][j] = dp[L][j] + abs(yin[i] - yin[i-1]);
      }
      
      L ^=1, C^=1;
   }

   // 找出最小的dp[i][i]
   int min_num = dp[L][0];
   for(int j = 1; j < yin.size()-1; j++){
       min_num = min(dp[L][j],min_num);
   }

   return min_num;
}

int main(){
    //int n=23;
    /*cin>>n;    
    int arr=new int[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }*/
    //vector<int> arr={24,13, 2, 4, 54, 23, 12, 53, 12, 23, 42, 13, 53, 12, 24, 12, 11, 24, 42, 52, 12, 32, 42};
    int n=5;
    vector<int> arr={1,5,6,2,1};
    if(n!=arr.size()){
        cout<<0;
        return 0;
    }

    cout<<song_min(n,arr,true)<<endl;
    cout<<zuihe(arr)<<endl;
    cin>>n;
    return 0;
}