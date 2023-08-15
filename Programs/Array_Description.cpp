#include <bits/stdc++.h>
using namespace std;


int main()
{
  
  long long n, k;
  cin >> n >> k;
  vector<long long> a(n);
  vector<long long> b(n);
 

  vector<pair<long long, long long>> v;
  long long x,y;
  for (long long i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
    
  }
  vector<vector<long long>> dp(n ,vector<long long>(k + 1,0));
  if(a[0]==0){
    for (long long i = 1; i <= k;i++){
      dp[0][i] = 1;
    }
  }
  else{
    dp[0][a[0]]=1;
  }
  for (long long i = 1; i < n; i++)
  
  {
    if(a[i]==0){
    for (long long j =1; j <=k; j++){
      dp[i][j] = (dp[i-1][j - 1] + dp[i][j]+dp[i-1][j])%1000000007;

      if (j + 1 <= k)
      {

        dp[i][j] = (dp[i-1][j + 1] + dp[i][j])%1000000007;
        }
    }
     
  }
    else{
        dp[i][a[i]] = (dp[i][a[i]] + dp[i-1][a[i] - 1]+dp[i-1][a[i]])%1000000007;
        if (a[i] + 1 <= k)
        {

          dp[i][a[i]] = (dp[i][a[i]] + dp[i-1][a[i] + 1])%1000000007;
        }
    
    }
    
  }
  
  long long ans = 0;
  for (long long i = 1; i <= k;i++){
  ans += (dp[n - 1][i])%1000000007;
  ans = ans % 1000000007;
  }
  cout << ans%1000000007;
}