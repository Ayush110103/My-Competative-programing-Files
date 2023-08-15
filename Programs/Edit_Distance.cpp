#include <bits/stdc++.h>
using namespace std;


int main()
{
  string s, t;
  cin >> s;
  cin >> t;
  int n = s.length();
  int m = t.length();
  long long dp[n + 1][m + 1];
  for (int i = 0; i < n + 1; i++)
  {
    for (int j = 0; j < m + 1; j++)
    {
      if (i == 0)
        dp[i][j] = j;
      else if (j == 0)
        dp[i][j] = i;
      else if (s[i - 1] == t[j - 1])
        dp[i][j] = dp[i - 1][j - 1];
      else
      {
        dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
      }
    }
  }
  cout << dp[n][m];
}