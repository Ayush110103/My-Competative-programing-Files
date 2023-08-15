
#include <bits/stdc++.h>
using namespace std;
int main()
{
  // int n;
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  vector<int> b(m);
  int x;
  set<pair<int, int>> s;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
    s.insert({a[i], i + 1});
  }
  for (int i = 0; i <m; i++)
  {
    cin >> x;
    b[i] = x;
  
  }

  int i = 0,j=0;
  
  while(i<m){
    auto match = s.lower_bound({b[i] + 1, 0});
    if(match==s.begin()){
      cout << -1 << endl;
      i++;
    }
    else{
      match--;
      cout << match->first << endl;
      s.erase(match);
      i++;
    }


  }
  
  
}
