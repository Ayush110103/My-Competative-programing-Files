#include <map>
#include <cmath>
#include <queue>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 2e5 + 10;

int n;
bool st[N];
int d[N];
vector<int> a[N];

int dfs(int u)
{
	bool ans = 0;

	if(d[u] == 1) 
		ans = 1;
	st[u] = true;
	for(auto v : a[u])
	{
		if(!st[v]) 
			ans += dfs(v);
	}
	return ans;
}

void Solve()
{
	cin >> n;
	memset(st,0,sizeof(st));
	memset(d,0,sizeof(d));
	for(int i = 0;i <= n;i++)
		a[i].clear();

	for(int i = 1;i <= n;i++)
 	{
 		int x;
 		cin >> x;
 		if(find(a[i].begin(),a[i].end(),x) == a[i].end())
 		{
 			d[x]++;
 			d[i]++;
		}
 		a[i].push_back(x);
 		a[x].push_back(i);
	}
	int ans1 = 0;
	int ans2 = 0;
	for(int i = 1;i <= n;i++)
	{
		if(!st[i])
		{
			ans1++;
			ans2 += dfs(i);
		}
	}
	cout << (ans1 - ans2) + (ans2 >= 1) << " " << ans1 << '\n';
}

int main()
{
    ios::sync_with_stdio(false),cin.tie(0);

    int t = 1;
    // cin >> t;
    while(t--)
        Solve();

    /*while(t--)
    {
        if(Solve)
            cout << "Yes" << '\n';
        else
            cout << "No" << '\n';
    }*/

    return 0;
}