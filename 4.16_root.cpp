
#include <windows.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	/**
	* 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
	* @param n int整型
	* @param s string字符串vector
	* @return int整型
	*/
	vector<bool> bEnd;
	vector<vector<char>> path;
	vector<vector<int>>  ver;

	int add(string &s)
	{
		static int idx = 0;
		int p = 0;

		for (int i = 0; i<s.size(); i++) {
			bool bExist = false;
			int j = 0;
			if (path.size()>0) {}
			for (; j<path[p].size(); j++) {
				{
					if (path[p][j] == s[i]){
						bExist = true;
						p = ver[p][j];
						if (i == (s.size() - 1)) bEnd[p] = 1;
						break;
					}
				}
			}
			if (!bExist) {
				bEnd.push_back((i == (s.size() - 1)) ? 1 : 0);
				vector<char> pt;
				path.push_back(pt);    // 子节点引用, u--位权，也是路径下标
				vector<int> v;
				ver.push_back(v);     // 如果子节点为空，则创建子节点, 并设置为idx,引用值与原变量共享存储，变则同变
				path[p].push_back(s[i]);
				ver[p].push_back(++idx);
				p = idx;
			}
		}
		return 0;
	}

	int get_root_str(int p) {
		if (bEnd[p])
			return 1;
		else {
			int n = 0;
			for (int i = 0; i<ver[p].size(); i++)
				n += get_root_str(ver[p][i]);
			return n;
		}
	}
	int solve(int n, vector<string>& s) {
		// write code here
		/**/
		bEnd.push_back(0);
		vector<char> pt;
		path.push_back(pt);    // 子节点引用, u--位权，也是路径下标
		vector<int> v;
		ver.push_back(v);     // 如果子节点为空，则创建子节点, 并设置为idx,引用值与原变量共享存储，变则同变

		for (int i = 0; i<n; i++)
			add(s[i]);
		return get_root_str(0);
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