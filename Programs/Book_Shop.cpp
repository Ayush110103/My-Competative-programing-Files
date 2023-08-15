
#include <bits/stdc++.h>
using namespace std;


int main()
{
  
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  vector<int> b(n);
 

  vector<pair<int, int>> v;
  int x,y;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
    
  }
  for (int i = 0; i < n;i++){
    cin >> x;
    b[i] = x;
    
  }
  vector<vector<int>> dp(n + 1,vector<int>( k + 1,0));
  for (int i = 0; i < n;i++){
    for (int j = 1; j <= k;j++){
      dp[i + 1][j] = dp[i][j];
      if(j>=a[i])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - a[i]] + b[i]);
    }
    // cout << endl;
  }

  cout << dp[n][k] << endl;
}
