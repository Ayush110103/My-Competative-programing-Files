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
  for (long long i = 1; i < s+1; i++){
    for (long long j= 0; j < n; j++)
    {
      if(i>=a[j])
        dp[i] += dp[i - a[j]]%1000000007;
      dp[i] = dp[i] % 1000000007;
      
    }
    
  }
  cout << dp[s]%1000000007<< endl;
  
}