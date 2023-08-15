
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while(t--){
  int n;
  cin >> n;
  // int n, m;
  // cin >> n >> m;
  vector<int> a(n);
  vector<int> b(n);
  vector<pair<int,int>> f(n);
  int x;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
  }
  for (int i = 0; i < n;i++){
    cin >> x;
    b[i] = x;
  }
  for (int i = 0; i < n;i++){
    f[i].first = a[i];
    f[i].second = b[i];
  }
  sort(f.begin(), f.end());
  // for (int i = 0; i < n;i++){
  //   cout << f[i].first <<" "<< f[i].second<<endl;
    
  // }
  multiset<int> s;

  for (int i = 0; i < n;i++){
     if(s.size()==0){
       s.insert(f[i].second);
       continue;
     }
     auto it = s.lower_bound(f[i].first);
    //  cout << *it;
     if(it==s.begin()){
        s.insert(f[i].second);
        // cout << 0;
        continue;
     }
      
      s.erase(s.begin());
      s.insert(f[i].second);

  }
  for (auto it = s.begin(); it != s.end();it++){
      cout << *it << endl;
  }
      cout << s.size() <<"a"<< endl;
      }
}
