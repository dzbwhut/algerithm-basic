
#include <windows.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

 

int main()
{
	Solution slt;
	vector<string> s = { "a","ab","bc" };

	cout << slt.solve(3, s)<<endl;

	system("pause");
	return 0;
}