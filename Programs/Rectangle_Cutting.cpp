#include <bits/stdc++.h>
using namespace std;


int main()
{
  int n, m;
  cin >> n>>m;
  
  
  vector<vector<int>> dp(n+1,vector<int>(m+1,0));
  for (int i = 1; i < n + 1; i++)
  {
    for (int j = 1; j < m + 1; j++)
    {
      if(i==j){
        dp[i][j] = 0;
        // cout << dp[i][j] << " ";
        continue;
      }
      if(i==1){
        dp[i][j] = j-1;
      }
      else if(j==1){
        dp[i][j] = i-1;
      }
      else{
        int mini = INT_MAX;
        for (int k = 1; k < i;k++){
          mini = min(mini, dp[k][j] + dp[i - k][j]);
        }
        for (int k = 1; k < j;k++){
          mini = min(mini, dp[i][k] + dp[i][j - k]);
        }
        dp[i][j] = mini + 1; 
        
      }
      // cout << dp[i][j] << " ";

    }
    // cout << endl;
  }
  cout << dp[n][m];
}