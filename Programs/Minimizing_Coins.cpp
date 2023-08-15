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
  vector<long long int> dp(s+ 1, 1e9);
  dp[0] = 0;
  long long c = 1e9;
  for (long long j= 0; j < n; j++){
  for (long long i = 1; i < s+1; i++)
    
    {
      if(i>=a[j])
        dp[i] = min(dp[i],1+dp[i - a[j]]);
    } 
  }
  if(dp[s]==1e9){
    cout << -1 << endl;
  }
  else{
    cout << dp[s]<< endl;
  }
  
  
}