//#include <windows.h>
#include <iostream>
#include <vector>
//#include <climits>
//#include <cmath>
//#include <algorithm>
using namespace std;

#define INT_MAX 0x7ffffff

int main(){
    int N=4,M=24;
    //while(cin>>N>>M){
        vector<int> steps(M+1,INT_MAX);
        steps[N] = 0;
        for(int i=N;i<=M;i++){
            if(steps[i] == INT_MAX){
                continue;
            }
            for(int j=2;(j*j)<=i;j++){
                if(i%j == 0){
                    if(i+j <= M){
                        steps[i+j] = min(steps[i]+1,steps[i+j]);
                    }
                    if(i+(i/j) <= M){
                        steps[i+(i/j)] = min(steps[i]+1,steps[i+(i/j)]);
                    }

                }

            }
        }
        if(steps[M] == INT_MAX){
            steps[M] = -1;
        }
        cout<<steps[M]<<endl;
    //}
    cin>>N>>M;
    return 0;
}