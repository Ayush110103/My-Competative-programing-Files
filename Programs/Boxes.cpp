
#include <bits/stdc++.h>
using namespace std;
bool cmp(int a1,int a2){

}
int main()
{
  int t;
  cin >> t;
  while(t--){
  int n;
  cin >> n;
  vector<int> a(n);
  int x;
  for (int i = 0; i < n;i++){
    cin >> x;
    a[i] = x;
  }
  sort(a.begin(), a.end());
  reverse(a.begin(), a.end());
  int ans = 1;
  multiset<int> s;
  s.insert(a[0]);
  for (int i = 1; i < n;i++){
    auto it = s.lower_bound(a[i]);
    if(it==s.end()){
      ans++;
      s.insert(a[i]);
    }
    else{
      s.erase(it);
      s.insert(*it ^ a[i]);
    }
    // s.insert(a[i]);
  }
  cout << ans << endl;
  }
}
