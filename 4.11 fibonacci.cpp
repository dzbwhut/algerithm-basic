#include <windows.h>
#include <iostream>
#include <math.h>

using namespace std;

const int P=1000000007;

class Matrix22{
    public:
        int m[2][2];
        Matrix22(int x=0) {
            if (x == 0) {
                m[0][0] = m[0][1] = m[1][0] = m[1][1] = 0;
            }
            else{
                m[0][0] = m[1][1] = 1;
                m[0][1] = m[1][0] = 0;
            }
        }

        Matrix22(int a, int b, int c, int d) {
            m[0][0] = a;
            m[0][1] = b;
            m[1][0] = c;
            m[1][1] = d;
        }

        Matrix22 operator *(const Matrix22 &b) {
        Matrix22 c(0);
        for(int i=0;i<2;i++) {
            for(int j=0;j<2;j++) {
                for(int k=0;k<2;k++) {
                    c.m[i][j] = (c.m[i][j] +(long long)(m[i][k] * b.m[k][j]))%P;
                }          
            } 
        }
        return c;
    }
};

//fn=[f1 f2]*M^(i-2) ≈ a[0,:]*a^(i-2)  ≈ a^(i-1)
Matrix22 power(Matrix22 M, long long n) {    
    Matrix22 res(1);//Identity matrix
    while (n) {
        if (n & 1) {
            res = res * M;
        }
        M = M * M;
        n >>= 1;
    }

    return res;
}

int main()
{
    Matrix22 a(1,1,1,0);
    Matrix22 c;
    
    /*int n;
    cin >> n;
    cout << power(a, n-2) << endl;
    */
    cout << " test fibonacci:  " << endl<<"    1) 1~10:  ";
    for(int i=1;i<10;i++) {
        c=power(a, i-1);//应－2：   实－1 ：[1 1]*a^(i-2) ≈ a[0,:]*a^(i-2)  ≈ a^(i-1)
        cout << c.m[0][0] << " ";        
    }
    unsigned long long n=1e18-1;
    cout << endl<<"    "<<n<< ")\t";
    c = power(a, n);
    cout << (long long)(c.m[0][0]) << endl;
    n=1e16;
    cout << endl<<"    "<<n<< ")\t";
    c = power(a, n);
    cout << (long long)(c.m[0][0]) << endl;
    cin>>c.m[0][1];
    return 0;
}
