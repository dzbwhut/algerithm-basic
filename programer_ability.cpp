/*  ��Ŀ������ ����һ������A[0,1,...,n-1], 
                �빹��?һ������B[0,1,...,n-1],����B�е�Ԫ��
                B[i]=A[0]A[1]...A[i-1]A[i+1]...A[n-1]�� 
                ?��ʹ?�ó�����
    ��     �⣺1��������:  ���������ˣ�ʱ�䣺O(n^2)���ռ䣺O(1)
               2���Ż��⣺ ������ң�ʱ�䣺O(n)���ռ䣺O(1)
                        B[i]��A[0]A[1]...A[i-1]  |   A[i+1]...A[n-1]�� 
                        ��-������B[i]=A[0]A[1]...A[i-1]
                        �Ҳ�-������B[i]*=A[i+1]...A[n-1]��
*/
#include <Windows.h>
#include <iostream>
#include <string>
#include <stdio.h>
//#include <stl>

using namespace std;
template<class T>
int getArrayLen( T & arr)
{
    return (sizeof(arr))/(sizeof(arr[0]));
}

template<int n>
int  multiply_by_A_store(int A[],int (& B)[n])
{
    //int[] B=new int[n];
    int i;
    B[0]=1;
    for(i=1;i<n;i++)
    {
        B[i]=A[i-1]*B[i-1];        
    }

    for(i=n-2;i>=0;i--)
    {
        A[i]=A[i]*A[i+1];        
    }

    for(i=0;i<n-1;i++)
    {
        B[i]=B[i]*A[i+1];        
    }
    
    return 0;
}
//#define unsigned long  ULONG
template<class T,int n>
int  multiply(T (& A)[n], T (& B)[n])
{
    int i;
    B[0]=1;
    for(i=1;i<n;i++)
    {
        B[i]=A[i-1]*B[i-1];        
    }

    T tmp = A[n-1];
    for(i=n-2;i>=0;i--)
    {
        B[i] *= tmp;     
        tmp *= A[i];  
    }
    
    return 0;
}

#define ARRAY_LEN  12
template<class T1, class T2,int m,int n>
int __test_arry_multiply(T1 (&A)[m],T2 (&C)[n])
{
    //unsigned long A[ARRAY_LEN], B[ARRAY_LEN];
    T1 B[m];
    T2 D[n];
    int i;

    multiply(A, B);
    multiply(C, D);

    cout<< "    ****** 1) ULONG:  ****** "<<endl<<endl;
    for(i=0;i<m;i++)
        printf("%3u - %8x\t",A[i], B[i]);
    cout<<endl<<endl<<"    ****** 2) Double:  ****** "<<endl<<endl;
    for(i=0;i<n;i++)
        printf("%2.8f - %4.10f\t",C[i], D[i]);

    return 0;
}

int test_arry_multiply(){
    unsigned long A[ARRAY_LEN*2];
    for(int i=0;i<ARRAY_LEN*2;i++)
    {   
        A[i] = i+1;        
    }

    double C[ARRAY_LEN];
    double s=0.2;
    for(int i=0;i<ARRAY_LEN;i++)
    {   
        C[i] = 1+ s;
        s*=0.95;
    }
   
    return  __test_arry_multiply(A,C);
}
// add new argerithm
typedef enum __argerithm{
    MULTIPLY_ARRAY=0,

    // add new argerithm
    ALGERITHM_LEN
}ALGERITHM_EN;

string FunctionDescription[]= {
    "1. �������� \n\
    ��Ŀ����: ����һ������A[0,1,...,n-1], \n\
                �빹��?һ������B[0,1,...,n-1],����B�е�Ԫ��\n\
                B[i]=A[0]A[1]...A[i-1]A[i+1]...A[n-1]�� \n\
                ����ʹ�ó�����\n\
                \n\
    ��     ��: 1��������:  ���������ˣ�ʱ�䣺O(n^2)���ռ䣺O(1)\n\
               2���Ż��⣺ ������ң�ʱ�䣺O(n)���ռ䣺O(1)\n\
                        B[i]��A[0]A[1]...A[i-1]  |   A[i+1]...A[n-1]�� \n\
                        ��-������B[i]=A[0]A[1]...A[i-1]\n\
                        �Ҳ�-������B[i]*=A[i+1]...A[n-1]��\n\
    ",

    "2. �������ظ������� \n\
    ��Ŀ����: ��һ������Ϊn����������������ֶ���0��n-1�ķ�Χ�ڡ�  \n\
            ������ĳЩ�������ظ��ģ�����֪���м������֣��ظ�����. \n\
            ���ҳ�����������һ���ظ������֡�\n\
            ����:{2,3,1,0,2,5,3}���ɷ���2��3 \n\
            \n\
    �ⷨ:\n\
            1�������������£�Ȼ������ұ��������������ڵ�����û����ȼ��ɡ�\n\
                ʱ��O(nlogn)���ռ�O(1).\n\
            2����һ����ϣ���������Щ���飬������Ԫ��ֵ��Ϊkey��\n\
               ��ͬԪ�صĸ�����Ϊ value�������Ĺ����У�\n\
               ֻҪ����ĳ��key��value����1����ô����������ظ����ˣ�ֱ�ӷ��ء�\n\
               ʱ��O(n)���ռ�O(n)��\n\
            3����ԭ�����Ϲ�ϣ,��ı�ԭʼ����(˳��)��  ʱ�䣺O(n),�ռ�:O(1)��\n\
    ",

    // add new argerithm script

    //end
    "\n"
};
template<class T1,class T2>
int swap(T1 a, T2 b)
{
    a^=b;
    b^=a;
    a^=b;
}

template<int n>
int array_replay(int (&a)[n])
{    
    for(int i=0;i<n;i++)
    {
        //int j=0;
        while(a[i]!=i )//&& j++<n
        {
            if(a[a[i]] == a[i])
            {
                return  a[i];
            }
            else
            {
               swap(a[i], a[a[i]]); 
            }
        }
    }
}

int test_arry_replay()
{
    int ar[]={2,3,1,0,2,5,3};
    int n=getArrayLen(ar);
    
    cout<< "  ----------�������ظ�������----  \n  1)  ";
    for(int i=0;i<n;i++)
        cout<<ar[i]<<", ";

    int m=array_replay(ar);    
    cout<<endl<<"\t---->\t"<<m<<endl;

    //3�����������
    int b[32];
    for(int j=0;j<5;j++){
        cout<<"  "<<j+1<<") ";
        for(int i=0;i<32;i++){
            b[i]=rand()%31;
            cout<<b[i]<<", ";
        }
        m=array_replay(b);
        cout<<endl<<"\t---->\t"<<m<<endl;
    }
    return 0;
}
int end();

//add a new function-pointer
int (*pf[])()={
    test_arry_multiply,
    test_arry_replay,
    //add a new function-pointer

    // last
    end
};

int end()
{
    cout<<"\r\b���ԣ� "<<getArrayLen(pf)-1<<"  �� ����"<<endl<<endl;
    return 0;
}

int main(int argc,char * argv[])
{
    int i=0, t = getArrayLen(FunctionDescription);
    //system("chcp 65001");
    //SetConsoleOutputCP(CP_utf8);
    cout<<endl<<"-----------����Ա�ڹ�����-------------------"<<endl<<endl;
    //argc=2;
    //argv[1]="1";
    if(argc<2 || (argv[1][0]=='-' && argv[1][1]=='h')){
        for(i=0;i<t;i++){
            cout<<FunctionDescription[i]<<endl<<">>  "<<endl;
            pf[i]();
            cout<<endl<<endl;
        }
    }else if(argc>2 ){ //|| (argv[2][0]=='-' && argv[2][0]=='-' && argv[2][1]=='h')
        cout<<FunctionDescription[atoi(argv[1])]<<endl;
    }
    else{
        try{      
            cout<<FunctionDescription[atoi(argv[1])]<<endl<<"\t�����  "<<endl; 
            pf[atoi(argv[1])]();
        }catch(exception & e){
            cout<<e.what() <<"Err: "<<FunctionDescription[atoi(argv[1])]<<endl;
        };
    }
    
    system("pause");

    return 0;
}