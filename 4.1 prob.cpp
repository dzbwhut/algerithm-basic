#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>

using namespace std;

#define RAND_MAX   ((float)32767)

int random01p(float p=0.1){    
    return rand()/RAND_MAX>p?1:0;
}

void test_random01p(int n=1e3, float p=0.1){
    int r[2]={0,0};
    for(int i=0;i<n;i++){
        r[random01p(p)]++;
    }

    cout<<"p="<<p<<" 0- "<<r[0]<<"  1- "<<r[1]<<endl;

    return;
}

int equiprobable01(float p=0.2){
    int ans;
    do{
        ans = random01p(p);
    }while(ans == random01p(p));

    return ans;
}

int equiprobable01_rand(){
    return rand()>RAND_MAX/2.0?1:0;    
}

void test_prob(int n, float p=0.2){
    int r[2][2]={0,0,0,0};
    for(int i=0;i<n;i++){
        r[0][equiprobable01(0.2)]++;
        r[1][equiprobable01_rand()]++;
    }
    cout<<" equiprobable-"<<p<<": 0 --"<<r[0][0]<<" 1--"<<r[0][1]<<endl;    
    cout<<" equiprobable_rand : 0 --"<<r[1][0]<<" 1--"<<r[1][1]<<endl;
    return ;
}

int probable01p2x(float x=0.7, float p=0.2, int n=10){
    //static_assert(x>=0 && x<=1);
    //static_assert(p>=0 && p<=1);
    int y=pow(2,10)*x;
    int ans=0;   

    while(n--){
        ans<<=1;
        ans += equiprobable01_rand();        
    }
    //cout<<"ans: "<<ans<<"  y: "<<y<<endl;
    return ans<y?0:1;
}

int probable01p2x_2(float x=0.7, float p=0.2, int n=10){
    //static_assert(x>=0 && x<=1);
    //static_assert(p>=0 && p<=1);
    
    float q=.5,ans=0.0;

    while(n--){
        ans +=q*equiprobable01(p);
        q*=.5;
    }
    //cout<<"ans: "<<ans<<"  x: "<<x<<endl;
    return ans<x?0:1;
}

void test_probable01p2x(int t=1e3, float p=0.1, float x=0.7,int n=10){
    int r[3][2]={0};
    clock_t startTime[3], endTime[3];
	
    startTime[2] = clock();
    for(int i=0;i<t;i++){ 
        r[0][random01p(p)]++;
    }
    
    endTime[2] = clock();
    float t1=(float)(endTime[2]-startTime[2]);// /(CLOCKS_PER_SEC/1e6);

    startTime[0] = clock();
    for(int i=0;i<t;i++){         
        r[1][probable01p2x(x,p)]++;       
    }
    endTime[0] = clock();
    float t3=(float)(endTime[0]-startTime[0]);// /(CLOCKS_PER_SEC/1e6);

    startTime[1] = clock();
    for(int i=0;i<t;i++){ 
        r[2][probable01p2x_2(x,p)]++;       
    }
    endTime[1] = clock();
    float t2=(float)(endTime[1]-startTime[1]);// /(CLOCKS_PER_SEC/1e6);

    cout<<" probable convert: p-->x  CLOCKS_PER_SEC="<<CLOCKS_PER_SEC<<endl;
    cout<< " p-"<<p<<": 0 --"<<r[0][0]<<" 1--"<<r[0][1]<<"  t: "<<t3<<" ms  s:"<<startTime[2]<<" e:"<<endTime[2]<<endl;
    cout<< " x-"<<x<<": 0 --"<<r[1][0]<<" 1--"<<r[1][1]<<"  t: "<<t1<<" ms  s:"<<startTime[0]<<" e:"<<endTime[0]<<endl;
    cout<< " x-"<<x<<": 0 --"<<r[2][0]<<" 1--"<<r[2][1]<<"  t: "<<t2<<" ms  s:"<<startTime[1]<<" e:"<<endTime[1]<<endl;

    return ;
}

int probableA2B(int a, int b){
    int c=b-a+1;
    int num=1,d=c;
    
    while((d>>1)>0){
        num++; d>>=1;        
    }

    int ans=0;
    do{
        int t=num;
        ans=0;
        while(t){    
            ans<<=1;    
            ans+=equiprobable01(0.3);
            --t;
        }
    }while(ans>=c);
    
    return ans+a;
}
void test_probableA2B(int n, int a, int b){
    int v;
    vector<int>r(b-a+1,0);
    for(int i=0;i<n;i++){
        v=probableA2B(a, b);        
        r[v-a]++;
    }
    cout<<" test probableA2B("<<a<<", "<<b<<"):"<<endl;
    for(v=0;v<r.size();v++){
        cout<<v+a<<" --"<<r[v]<<endl;
    }
    
    return ;
}

float pi(int n=1e4)
{    
    float x=0,y=0,pai=0.0;
    int c=0;
    for(int i=0;i<n;i++){
        x=rand()/RAND_MAX;
        y=rand()/RAND_MAX;
        if(x*x+y*y<=1){
            c++;
        }
    }
    pai=4.0*c/n;
    return pai;
}
void test_pi(int n=5){    
    int j=1e3;
    for(int i=1;i<=n;i++){ 
        j*=4;
        cout<<i<<")  pi: "<<pi(j)<<"  "<<j<<endl;  
    }
    
    return ;
}
float exp(int n=1e4)
{    
    double x,y;
    int c=0;
    for(int i=0;i<n;i++){
        x=rand()/RAND_MAX+1.0;
        y=rand()/RAND_MAX;
        if(y<1/x){
            c++;
        }
    }

    return pow(2,(double)n/c);
}

double exp_series(int n=1e4)
{  // e=1+1/1!+1/2!+1/3!+...
    double e=1.0,p=1.0;
    //e=2.7182818284590452353602874713527;
    for(int i=1;i<=n;i++){
        p*=i;
        e+=1.0/p;
    }

    return e;
}

void test_exp(int n=5){    
    int j=2;
    for(int i=1;i<=n;i++){ 
        j*=5;
        printf("%2d)  e: %1.20f iter: %8d\n",i, exp(j), j);  
    }
     
    return ;
}

int main()
{
    int times = 1e4;
    int cases=5;

    srand(time(NULL));//设置随机数种子，使每次产生的随机序列不同

    switch (cases) {
        case 0:
            test_random01p(times,0.3);
            break;
        case 1:       
            test_prob(times,0.1);    
            test_prob(times); 
            test_prob(times,0.5);
            test_prob(times,0.8);
            test_prob(times,0.9);
            test_prob(times,0.99);
            break;    

        case 2:
            test_probableA2B(times, 2, 7);
            break;
        
        case 3:
            test_probable01p2x(times);
            break;

        case 4:
            test_pi(10);
            break;
            
        case 5:
            test_exp(10);
            break;

        default:
            break;
    }
    
    system("pause");
    return 0;
}

