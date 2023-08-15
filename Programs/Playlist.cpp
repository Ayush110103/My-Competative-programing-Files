
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  // int n, m;
  // cin >> n >> m;
  vector<int> a(n);
  int x;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
  }
  set<int> s;
  int ans = 1, i = 0,j=0;
  while (i < n && j < n) {
    
    while (j < n && s.count(a[j])==0) {
      s.insert(a[j]);
      ans = max(ans, j - i+1);
      j++;
    }
    
    while(j<n && s.count(a[j])){
      s.erase(a[i]);
      i++;
    }
    }
  
  cout << ans << endl;

     
  }


