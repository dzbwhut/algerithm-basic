// https://www.nowcoder.com/study/live/718/3/15
/* 题目：
    小易去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个每袋的包装(包装不可拆分)。 可是小易现在只想购买恰好n个苹果，小易想购买尽量少的袋数方便携带。如果不能购买恰好n个苹果，小易将不会购买。
  输入描述:
    输入一个整数n，表示小易想购买n(1 ≤ n ≤ 100)个苹果
  输出描述:输出一个整数表示最少需要购买的袋数，
    如果不能买恰好n个苹果则输出-1
  示例1： 输入  20  输出 3
题解：
  1) 暴力解： 贪心法：
  2) 笔试： 业务题,  输出暴力解，找规律
  3) 面试：规律及数学意义：

*/
#include <iostream>
#include <math.h>
//#include <windows.h>

using namespace std;

int buyApple_Od8_1(int n)
{
    int ans = -1;

    if (n >= 6)
    {
        int r = n % 8;
        for (int b = floor(n / 8); b >= 0; b--)
        {
            if (r % 6 == 0)
            {
                ans = (b + r / 6);
                break;
            }
            r += 8;
        }
    }

    return ans;
}

int buyApple_Od8_2(int n)
{
    int ans = -1;

    if (n < 6)
        return -1;
    else
    {
        int r = n % 8;
        for (int b = floor(n / 8); b >= 0; b--)
        {
            if (r % 6 == 0)
            {
                ans = (b + r / 6);
                break;
            }
            r += 8;
        }
    }

    return ans;
}

int buyApple_O1_1(int n)
{
    int ans = -1;

    if (n % 2 == 0 && n >= 6)
    {
        if (n > 10)
            ans = floor((n - 18) / 8.0) + 3;
        else if (n < 10)
            ans = 1;
    }
    return ans;
}

int buyApple_O1_2(int n)
{
    int ans = -1;

    if (n & 1 == 1 || n < 6 || n == 10) //奇偶：n%2==1，n&1==1
        ans = -1;
    else
        ans = floor((n - 18) / 8.0) + 3;

    return ans;
}

int main()
{
    int n, ans = -1;
    
    cin >> n;

    cout << "buyApple_Od8_1(n): " << buyApple_Od8_1(n) << endl;
    cout << "buyApple_Od8_2(n): " << buyApple_Od8_2(n) << endl;
    cout << "buyApple_O1_1(n): " << buyApple_O1_1(n) << endl;
    cout << "buyApple_O1_2(n): " << buyApple_O1_2(n) << endl;

    system("pause");
    return 0;
}