
#include <bits/stdc++.h>
using namespace std;
typedef long long  ll;
int main()
{
  // int n;
  // cin >> n;
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  int x;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
  }
  ll ans = 1e18;
  ll l = 0, r = 1e18;
  while(l<=r){
    ll mid = (l + r) / 2;
    ll sum = 0;
    for (int i = 0; i < n;i++){
      sum += min(mid / a[i],(ll) 1e9);
    }
    if(sum>=m){
    
      ans = min(ans, mid);
      r = mid - 1;
    }
    else{
      l = mid + 1;
    }
  }
  cout << ans << endl;
}
