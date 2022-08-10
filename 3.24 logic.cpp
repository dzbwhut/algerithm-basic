/* 逻辑组合数.   参考: https://www.cnblogs.com/grandyang/p/5271856.html */
#include <windows.h>
#include <iostream>

using namespace std;

const long long p = 1e9+7;

// 逻辑串S的合法性检测: n o n o ... n o n  
bool isValid(string s)
{
    if(s.size()&1==0)//长度是偶数false
        return false;

    for(int i=0;i<s.length()-1;i+=2){
        if ((s[i]=='1'|| s[i]=='0') && 
            (s[i+1]=='|' || s[i+1]=='&' || s[i+1]=='^'))

            continue;
        else  
            return false;
    }

    if (s[s.length()-1]=='1' || s[s.length()-1]=='0')
        return true;
    else
        return false; 
}

long long f_iter(string &s,int L,int R,bool bv) {    
    /* Function: 产生特定逻辑值的逻辑串的计算优先级的组合数.  

    Args: 逻辑组合数:LR范围搜索
        -s  逻辑串
        -bv 逻辑表达式的值：布尔值,true,false        

    Returns:
        int - 组合数
    */
    
    if (s.length()==0) return 0;    
    if(L>R)   return 0;

    if(L==R){
        if (s[L]=='1')  return bv?1:0;//1 if bv else 0
        else  return bv?0:1;//0 if bv else 1
    }    
        
    long long ans=0;        
    for(int i=L+1;i<R;i+=2){  
        if(bv){ // true
            if (s[i] == '&')
                ans +=(f_iter(s,L,i-1,true)*f_iter(s,i+1,R,true)%p);//TT 
            else if (s[i] == '|'){
                ans += (f_iter(s,L,i-1,true)*f_iter(s,i+1,R,true)%p);//TT;
                ans += (f_iter(s,L,i-1,true)*f_iter(s,i+1,R,false)%p);//TF;
                ans += (f_iter(s,L,i-1,false)*f_iter(s,i+1,R,true)%p);}//FT;
            else if (s[i] == '^'){
                ans  = (f_iter(s,L,i-1,true)*f_iter(s,i+1,R,false)%p);//TF;
                ans += (f_iter(s,L,i-1,false)*f_iter(s,i+1,R,true)%p);} //FT;                   
        }else{ // false
            if (s[i] == '&'){
                ans += (f_iter(s,L,i-1,false)*f_iter(s,i+1,R,true)%p);//FT;
                ans += (f_iter(s,L,i-1,true)*f_iter(s,i+1,R,false)%p);//TF;
                ans += (f_iter(s,L,i-1,false)*f_iter(s,i+1,R,false)%p);}//FF;
            else if (s[i] == '|'){
                ans += (f_iter(s,L,i-1,false)*f_iter(s,i+1,R,false)%p);} //FF;                  
            else if (s[i] == '^'){
                ans += (f_iter(s,L,i-1,true)*f_iter(s,i+1,R,true)%p);//TT;
                ans += (f_iter(s,L,i-1,false)*f_iter(s,i+1,R,false)%p);}//FF;
        }
        ans %= p;
    }
    return ans;
    
}

template<class Type> 
void make2DArray(Type ** &arr,int rows, int cols){
    /* Function: 生成一个数组.ws

    Args:
        -n  数组长度
        -a  初始值

    Returns:
        T[] - 数组
    */
    arr = new  Type *[rows];
    for(int i=0;i<rows;i++)
        arr[i]=new Type[cols];
    return ;
}

template<class Type> 
void delete2DArray(Type ** &arr,int rows){
    /* Function: 释放一个数组.  

    Args:        
        -arr  初始数组
        -rows 数组长度

    Returns:
        void - 数组
    */

    for(int i=0;i<rows;i++)
        delete[] arr[i];
    delete[] arr;
    arr=0;
}

//逻辑组合数:动态规划
long long f_dynamic_program(string &s, bool bv){
    /*产生特定逻辑值的逻辑串的计算优先级的组合数：动态规划.

    Args: 逻辑组合数:LR范围搜索
        -s  逻辑串
        -bv 逻辑表达式的值：布尔值,true,false        

    Returns:
        int - 组合数
    */
    if (s.length()==0)   return 0;

    long long **T;
    make2DArray(T,s.length(),s.length());
    long long **F;
    make2DArray(F,s.length(),s.length());
        
    for(int i=s.length()-1;i>=0;i-=2){
        for(int j=i;j<s.length();j+=2){
            if(i%2==1 || j%2==1)  continue;

            if (i==j){               
                if (s[i]=='1')       T[i][j]=1, F[i][j]=0;
                else if (s[i]=='0')  T[i][j]=0, F[i][j]=1;
            }else{    
                T[i][j]=0, F[i][j]=0;                
                for(int k=i;k<j;k+=2){ 
                    if (s[k+1] == '&'){
                        T[i][j]  += T[i][k]*T[k+2][j];
                        F[i][j]  += F[i][k]*F[k+2][j];
                        F[i][j]  += F[i][k]*T[k+2][j];
                        F[i][j]  += T[i][k]*F[k+2][j];
                    }else if (s[k+1] == '|'){
                        T[i][j]  += T[i][k]*T[k+2][j];
                        T[i][j]  += T[i][k]*F[k+2][j];
                        T[i][j]  += F[i][k]*T[k+2][j];
                        F[i][j]  += F[i][k]*F[k+2][j];
                    }else if (s[k+1] == '^'){
                        T[i][j]  += T[i][k]*F[k+2][j];
                        T[i][j]  += F[i][k]*T[k+2][j];
                        F[i][j]  += F[i][k]*F[k+2][j];
                        F[i][j]  += T[i][k]*T[k+2][j];
                    }

                    T[i][j]=(long long)(T[i][j]%p);
                    F[i][j]=(long long)(F[i][j]%p);                    
                }
            }
        }
    }
    
    long long ans= bv?T[0][s.length()-1]:F[0][s.length()-1];
    
    delete2DArray(T,s.length());
    delete2DArray(F,s.length());

    return ans;
}

unsigned long long t[500][500];
unsigned long long f[500][500];

unsigned long long f_dynamic_program_2(string &s, bool bv){
    /*产生特定逻辑值的逻辑串的计算优先级的组合数：动态规划.

    Args: 逻辑组合数:LR范围搜索
        -s  逻辑串
        -bv 逻辑表达式的值：布尔值,true,false        

    Returns:
        int - 组合数
    */
   
    for(int i=0;i<s.size();i+=2)
    {
        t[i][i]=(s[i]=='0'? 0:1);
        f[i][i]=(s[i]=='0'? 1:0);
    }
      
    unsigned long long sum_t,sum_f;
    for(int len=2;len<s.size();len+=2)
    {
        for(int i=0;i+len<s.size();i+=2)
        {   
            sum_t=0;
            sum_f=0;
            for(int j=i+1;j<i+len;j+=2)
            {
                if(s[j]=='&')
                {
                    sum_t+=(t[i][j-1]*t[j+1][i+len])%p;
                    sum_f+=((t[i][j-1]*f[j+1][i+len])+
                           (f[i][j-1]*t[j+1][i+len])+
                           (f[i][j-1]*f[j+1][i+len]))%p;
                }
                else
                    if(s[j]=='|')
                    {
                        sum_t+=((t[i][j-1]*t[j+1][i+len])+
                               (t[i][j-1]*f[j+1][i+len])+
                               (f[i][j-1]*t[j+1][i+len]))%p;
                        sum_f+=(f[i][j-1]*f[j+1][i+len])%p;
                    }
                     else
                     {
                         sum_t+=((t[i][j-1]*f[j+1][i+len])+
                                (f[i][j-1]*t[j+1][i+len]))%p;
                         sum_f+=((t[i][j-1]*t[j+1][i+len])+
                                (f[i][j-1]*f[j+1][i+len]))%p;
                     }
            }
            t[i][i+len]=(sum_t%p);
            f[i][i+len]=(sum_f%p);
        }
    }

    if(bv)
        return  t[0][s.size()-1];
    else
        return  f[0][s.size()-1];    
}

int main(void)
{
    string s[]={"1^0|0|1",
                "0^1^1|1^0&0|1|0&0^1&1|1&1^1|0&1|1&0&1|0|0^0&0|1^1^1&1^0^1|1|0^1^1|0&1&1|0&1|1|0&0&1|0^0&0^1|1^1^0&0&0&1&0|1|1|0&1^1&0&0&1&0|1|1^1|1|0|1^1^1|0|0^1&0&0^0^0|1^1^0^0^0&0^0|1|1&0^1^0|1|1|0&0|1^0&0&0&1|0&0&0&0^1^1|0|1|1|1&0|1^1^1^0^1&1|0&0&1^1&1^1|1^1|0|0|1^1&0^0^1|1&0^1|1|1|1|1^1^1^1&0^0|0&0&0&0|1&0^1^1|1^0^0|0^1^0^0&1|1^1&1&1|0^0&0&0^0&0&0|0^1&0&0^1|0^1^0|1|0^0|0&1|0^0|1|0^0^1|1^1^1&1&1|1|0|1|1&0^0&1^1|0&0&0&1^0|0^1^1|0|0&0&0^0^0&0&1&1|0^0|0&1|1^0^0|1^0|0^1^0&0|0^1&0&0|0|0^1|0&1|0|0|1^1|0|1|1^1|1&0",
                "0^0^1&0&1&0|0&0|1&0^0&1^0&1|0|0&0|0|1|1^0|1|1&0^1^0|0&1&1&1&0^0^1|1|1^0|1|0^0^0|1|1^0|1^0|0|1^0|0&0^1^0^0|1|0&1|1^1^1&0&0&0|0^1&0^1^1&1&0^0^1|1&0|0^1&1|0|1&0|1&0|0&1^1&0|1|1|0&1&0&0&0|0^0^1&0^0^0^0&1|1^1&1^1|0&0&1&1&1&1&1^1|0|1&1^0^0|1|0|0^1^1&0^0^0|0^1|0|1^0|1|0^1&0&1^1&1^1|1^0|1&0^0|1&0^1|0^1^0&1^0&0|0|0&0|0^1&1|0&1^1&0&0&1&0&0^1&0|0^0|0^1^0&0|0^1&1&0|0^0|0^1^0|0|1^0&1&0^1|1^1^1|1&1^1^0&0^0|1&0|0|0&0&0&1^0|1|1^1&1&0^1^1^1^0&0|0^0|0|0^0|0|1^1^0&1|1&1|0^1|1^0^1|1^0^1|1|1&0&1&1|1^0^0&1&1^0|1&1^0"
                };
    bool bv[]={false,true,false};
    long long v[]={2,130174822,66719894};
    //print('iter: ',f_iter(s,bv))
    long long ans1=0,ans2=0,ans3=0;
    for(int i=0;i<3;i++)
    {
        //f_iter(s,0,s.length()-1,bv);
        ans2=f_dynamic_program(s[i],bv[i]);
        ans3=f_dynamic_program_2(s[i],bv[i]);
        cout<<"iter: "<< ans1 <<"    dynamic: "<<ans2<< "    dynamic-2: "<<ans3<<" ==? " << v[i] << endl;
    }
    
    system("pause");
    return 0;
}