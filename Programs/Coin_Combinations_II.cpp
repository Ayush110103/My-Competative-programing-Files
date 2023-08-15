#include <bits/stdc++.h>
using namespace std;
int main()
{
  long long n,s;
  cin >> n>>s;
  vector<long long> a;
  for (int i = 0; i < n; i++)
  {
    long long x;
    cin >> x;
    a.push_back(x);
  }
  vector<long long int> dp(s+ 1, 0);
  dp[0] = 1;
  for (long long i = 0; i < n;i++){
    for (long long j = 1; j < s + 1;j++){
      if(j>=a[i])
        dp[j] += dp[j - a[i]]%1000000007;
      dp[j] = dp[j] % 1000000007;
    }
    // cout << dp[s];
  }
  cout << dp[s]%1000000007<< endl;
}