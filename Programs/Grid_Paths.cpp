#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  // int n, m;
  // cin >> n >> m;
  string a[n];
  string  x;
  long long dp[n][n];
  for (int i = 0; i < n;i++){
    string s;
    cin >> s;
    a[i] = s;
    }
  // for (int i = 0; i < n;i++){
  //   cout << a[i];
  // }
  for (int i = 0; i < n;i++){
    for (int j = 0; j < n;j++){
      if(a[i][j]=='*')
        dp[i][j] = 0;
      else if(i==0&&j==0)
        dp[i][j] = 1;
      else if(i==0)
        dp[i][j] = dp[i][j - 1];
      else if(j==0)
        dp[i][j] = dp[i - 1][j];
      else{
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
      dp[i][j] = dp[i][j] % 1000000007;}
    }
  }
  cout << dp[n - 1][n - 1];
}
