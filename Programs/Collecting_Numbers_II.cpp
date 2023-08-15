
#include <bits/stdc++.h>
using namespace std;
int main()
{
  // int n;
  // cin >> n;
  int n, m;
  cin >> n >> m;
  vector<int> a(n+1);
  vector<int> pos(n + 1);
  int x;
  for (int i = 1; i < n+1;i++){
    cin >> x;
    a[i] = x;
    pos[x] = i;
  }
  int ans = 1;
  for (int i = 2; i < n+1;i++){
    if(pos[i]<pos[i-1])
      ans++;
  }
  int l, r;
  set<pair<int, int>> pairs;
  while(m--){
    cin >> l >> r;
    if(a[l]+1<=n){
      pairs.insert({a[l], a[l] + 1});
    }
    if(a[l]-1>=1){
      pairs.insert({a[l]-1, a[l]});
    }
    if(a[r]+1<=n){
      pairs.insert({a[r], a[r] + 1});
    }
    if(a[r]-1>=1){
      pairs.insert({a[r]-1, a[r]});
    }
    for (pair<int,int> swapped:pairs){
      ans -= pos[swapped.first] > pos[swapped.second];
    }
    swap(a[l], a[r]);
    pos[a[l]] = l;
    pos[a[r]] = r;
    for(pair<int,int> swapped:pairs){
      ans += pos[swapped.first] > pos[swapped.second];
    }
    cout << ans << endl;
    pairs.clear();
  }
  
}
