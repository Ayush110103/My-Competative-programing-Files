#include <bits/stdc++.h>
using namespace std;


int main()
{
  int n;
  cin >> n;
  
  
    vector<int> a(n);
    int x;
    int s = 0;
    for (int i = 0; i < n;i++){
      cin >> x;
      a[i] = x;
      s += a[i];
    }

    vector<long long> dp(s+1,0);
    dp[0] = 1;
    for (int i = 0; i < n;i++){
      for (int j = s; j >0; j--)
      {
        if(j-a[i]>=0){
          dp[j] += dp[j - a[i]];
        }

      }
    
    }
    int c = 0;
    for (int i = 1; i < s+1;i++){
      if(dp[i]!=0){
        c++;
      }
    }
    cout << c << endl;
    for (int i = 1; i < s+1;i++){
      if(dp[i]!=0){
        cout << i << " ";
      }
    }

}