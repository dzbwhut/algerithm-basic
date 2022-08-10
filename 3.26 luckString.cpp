/*
// 求最长幸运字符串
// 小A很喜欢字母N，他认为连续的N串是他的幸运串。
// 有一天小A看到了一个全部由大写字母组成的字符串，
// 他被允许改变最多2个大写字母（也允许不改变或者只改变1个大写字母），
// 使得字符串中所包含的最长的连续的N串的长度最长。
'''
1 2 3 4 5 6 7 8 9 10 11 12 13
1 1 2 4 3 3 9 6 6  9  5  7 49 37 32 53 45 49 8 8
1 1 2 4 3 2 9 6 4  8  5  7 45 37 32 53 45 49 8 8
          6 7   9 10

6 NAN
9 NNNNBB
10 NNNNBNNNN
'''
se=["O","ANA","NAN","NNNNBB","NNNNBNNNN"]
*/
#include <vector>
#include <iostream>
#include <windows.h>
#include <string>

using namespace std;

int luck_string_max_clear(string ds){
    vector<int> ns={0}; //N串的长度
    vector<int> ss;//间隔串的长度
    int k=0; //N串的编号
    int j=-1; //间隔串的编号
    
    if(ds.size()<1)   return 0;
        
    //确保交叉序列 :  “ns”,ss,ns,ss    
    if(ds[0]=='N')   ns[k]+=1;
    else             ss.push_back(1),j++; //“ss”开始,增加ns[0]=0
        
    //遍历ds串
    for(int i=1;i<ds.size();i++) {
        if(ds[i]=='N'){
            if(ds[i-1]!='N')   ns.push_back(0),++k;  
            ns[k]+=1; 
        }   
        else{
            if(ds[i-1]=='N') ss.push_back(0), ++j;            
            ss[j]+=1;
        }
    }

    //计算最大长度--遍历ns:  ns初始化为[0]         
    int maxN=0;  // N串的最大长度
    int lr=0;
    for(int i=0; i<ns.size();i++){// N串存在
        lr=ns[i];
        if(ss.size()>i){ //右侧   ss[i]存在："...Nccc"            
            lr += min(2,ss[i]); // NS[i] + SS[i]
            if(ss[i]<=2 && ns.size()>i+1){ //如果当前N串的间隔串的长度小于等于2，则可以拼接
                lr += ns[i+1];  // NS[i] + 1s/2s + NS[i+1]                 
                if(ss[i]==1){// NS[i] 1s NS[i+1]，后续的N串，S串，可以拼接 
                    if(ss.size()>i+1){ //ss[i+1]存在
                        lr += 1; //NS[i] 1s NS[i+1] 1s
                        if(ss[i+1]==1 && ns.size()>i+2) //如果当前N串的间隔串的长度为1，且下一个N串的间隔串的长度为1，则可以拼接
                            lr += ns[i+2]; //NS[i] 1s NS[i+1] 1s NS[i+2]
                        // else)  
                        //   NOP     //ss[i+1]>1 不可以拼接；NS[i+2]不存在，无串可拼接  
                    }
                    else if(i>0) //ss[i+1]不存在，ss[i-1]存在
                        lr += 1; // 1s NS[i] 1s NS[i-1]
                    
                // else:  NS[i] + 2s + NS[i+1]  
                //   NOP     //ss[i]>=2 后续串不再拼接 
                }
            }
            else if(ss[i]==1 && i>0) //如果当前N串的间隔串的长度为2，且下一个N串的间隔串的长度为1，则可以拼接
                lr += 1;
        }
        else if(i>0)//右侧没ss[i]--末尾的N串，且非头，右侧不存在ss，左侧存在："...cccN"
            lr += min(2,ss[i-1]);    

        maxN=max(maxN,lr);
    }

    if(ns.size()==0 && ss.size()>0)//N串不存在，只有间隔串
        maxN=min(2,ss[0]);

    return maxN;      
}


// 输出最长幸运字符串，少用存储空间，一次遍历
int luck_string_max_opt(string ls)
{
    int sz=ls.size();
    if(sz<=2)   return min(sz,2);

    vector<int> ns={0}; //N串的长度    
    int k = 0;

    for(int i=0;i<sz;i++){                
        if(ls[i]=='N') {
            ns[k]+=1;
            if(i<sz-1 && ls[i+1]!='N')   ns.push_back(0),++k;
        }
        else {
            ns[k]-=1;
            if(i<sz-1 && ls[i+1]=='N') ns.push_back(0), ++k;
        }    
    }   
    if(ns[ns.size()-1]<0) ns.push_back(0);

    k=2;
    for(int i=0;i<ns.size();i++){
        if(ns[i]<0) continue;
        
        int ln=ns[i]; //NS                 
        if(i>0){ 
            ln+=min(2,-ns[i-1]); //SS1/2 + NS
            if(i>1 and -ns[i-1] <=2 ){ // S1 + NS
                ln +=ns[i-2];     //NS  +(SS1/2 + NS)  
                if(i>2 && -ns[i-1]==1){  //SS1/2 
                    ln +=1;  // 1s + (NS + S1 + NS) 
                    if( i>3 && -ns[i-3]==1) ln += ns[i-4]; // NS + (S1 + NS  + S1 + NS)
                }
            }
            //else: ns(i-1)不存在，ns[i-2]>2,后续不可以拼接  -3 + NS
        }
        else if(ns.size()>1)    ln += min(2,-ns[i-1]); //NS + SS
        k=max(k,ln);       
    }
    
    return k;
}

int luck_string_max_ss(string s)
{
    int a[50010]={0},cnt=1,num=0;
    //memset(a,0,sizeof(a));
    
    for(int i=0;i<s.size();i++){
        if(s[i]!='N'){
            num++;
            if(a[cnt]<=0){
                a[cnt]--;
            }
            else{
                cnt++;
                a[cnt]--;
            }
        }
        else{
            if(a[cnt]>=0){
                a[cnt]++;
            }
            else{
                cnt++;
                a[cnt]++;
            }
        }
    }

    if(num<=2)    return s.size();        
   
    int ans=0;
    for(int i=1;i<=cnt+1;i++){
        if(a[i]<0){
            if(a[i]<-2){
                ans=max(ans,a[i-1]+2);
                ans=max(ans,a[i+1]+2);
            }
            else if(a[i]==-2){
                ans=max(ans,a[i-1]+2+a[i+1]);
            }
            else if(a[i]==-1){
                if(a[i+2]==-1){
                    ans=max(ans,a[i-1]+a[i+1]+a[i+3]+2);
                }
                else{
                    ans=max(ans,a[i-1]+a[i+1]+2);
                }
            }
        }
    }
    return ans;
}

int main()
{   
    //vector<string> se={"O","ANA","NAN","NNNNBB","NNNNBNNNN"};
    //int sz=se.size();
    //string se[]={"O","ANA","NAN","NNNNBB","NNNNBNNNN"};
    //int sz=sizeof(se)/sizeof(se[0]);
    char* se[]={"CNNHNQNBMNNQNNDVINNCNNHNNNINIRKNNZNRNUNNVMIZWRSNNNMFRDNUNYNWNNNFZLVNNFNNNNNBJHNZICDRYNVINONNNVLOMGPN",
        "O","ANA","NAN","NNNNBB","NNNNBNNNN","BBBNNNBBNNNCCNNNNDD",
        "NNANZAZNNGBGINGNLLRINVBNBJNQDNDBNNPJNNZHONTGLNYTNEJNNTTNNGNFKUEHXNNNEHNNNYINNNPSBINHGNSNTNLNNNQUSESN"};
    int sz=sizeof(se)/sizeof(se[0]);
    for(int i=0;i<sz;i++){
        cout<<i<<") "<<se[i]<<" "<<luck_string_max_clear(se[i]);
        cout<<" "<<luck_string_max_opt(se[i]);
        cout<<" "<<luck_string_max_ss(se[i])<<endl;
    }   
    
    system("pause");
    return 0;
}



