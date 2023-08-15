#include <bits/stdc++.h>
using namespace std;
int main()
{
  long long n;
  cin >> n;
  vector<long long> dp(n+1,0);
  dp[0] = 1;
  for (long long i = 1; i < n+1; i++){
    for (long long j = 1; j < 7;j++){
      if(i>=j)
        dp[i] += dp[i - j]%1000000007;
      dp[i] = dp[i] % 1000000007;
    }
  }
  cout << dp[n]%1000000007<< endl;
}