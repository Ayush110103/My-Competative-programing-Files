#include <bits/stdc++.h>
using namespace std;


int main()
{
  long long n;
  cin >> n;
  
  
    vector<long long> a(n);
    vector<long long> s(n+1);
    long long x;
    for (long long i = 0; i < n;i++){
      cin >> x;
      a[i] = x;
      
    }
    s[0] = 0;
    long long y = 0;
    for (long long i = 0; i < n; i++)
    {
      /* code */
      y += a[i];
      s[i+1] = y;
    }
    

    long long dp[n][n][2];
    for (long long i = 0; i < n;i++){
      dp[i][i][0]=a[i];
      dp[i][i][1] = 0;
    }
    long long i=0,j = 2;
    for (long long k= 0; k < n-1;k++){
      i = 0;
      j = k +1;
      while(j<=n-1){

    
        dp[i][j][0] = max(a[i] + dp[i + 1][j][1], a[j] + dp[i][j - 1][1]);
        dp[i][j][1] = s[j + 1] - s[i]-dp[i][j][0];
        // cout << dp[i][j][0] <<","<< dp[i][j][1] << " ";

        i++;
        j++;
      }
      // cout << endl;
    }
    cout << dp[0][n-1][0] << endl;
}

