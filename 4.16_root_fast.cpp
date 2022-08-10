#include <windows.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;
class Solution {
    static bool strCmpLen(const string& s1, const string& s2){
        if (s1.size() == s2.size())
            return s1[0] <= s2[0];
        return s1.size() <= s2.size();
    }
    static bool isPreStr(const string& s1, const string& s2){
        int i = 0, j = 0;
        while (i < s1.size())
        {
            if (s1[i++] != s2[j++])
                return false;
        }
        return true;
    }
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * @param n int整型
     * @param s string字符串vector
     * @return int整型
     */
     
    int solve(int n, vector<string>& s) {
        // write code here
        vector<int> ret(n,1);
         
        int ans = 0;
        sort(s.begin(), s.end(),strCmpLen);
        for (int i = 0; i < n; i++){
            if (ret[i] == 0)
                continue;
            for (int j = i+1; j < (n - 1);j++){
                if (s[j][0] != s[i][0])
                    break;
                if (isPreStr(s[i], s[j])){
                    ret[j] = 0;
                    if (s[i].length() == s[j].length()){
                        ret[i] = 0;
                    }
                }             
            }
            if (ret[i] == 1)
                ans++;
        }
        return ans;
    }
};

int main()
{
	Solution slt;
	vector<string> s = { "a","ab","bc" };

	cout << slt.solve(3, s)<<endl;

	system("pause");
	return 0;
}