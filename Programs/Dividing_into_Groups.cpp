#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while(t--){
  int n,k;
  cin >> n>>k;
  vector<int> a;
  set<int> s,s2;
  for (int i = 0; i < n; i++)
  {
    int x;
    cin >> x;
    a.push_back(x);
  }
  if(k>n){
    cout<<0<<endl;
    // cout << endl;
    continue;
  }
  int c = 0;
  sort(a.begin(),a.end());
  reverse(a.begin(), a.end());
  int i;
  for ( i = 0; i < k; i++)
  {
    s.insert(a[i]);

  }
  // i++;
  int ans = 0,t;

  while (true){
  if(s.size()>0){
  auto it = s.begin();
  ans += *it;
  // s = s - *it;
  s.erase(*(s.begin()));
  if (s.size()>0){
      for (auto k = s.begin(); k != s.end();k++){
        s2.insert(*k-*it);
        
        // cout << *k << " ";
      }
      // cout << s.size();
      
      s = s2;
      s2 = {};}

  
  if (s.size() < k)
  {
    if (i + (k - s.size()) - 1 > n - 1)
    {
      cout << ans<<endl;
      // cout << endl;
      break;
        }
    else
    {
      for (t = i; t < i + k - s.size(); t++)
      {
        /* code */
        s.insert(a[t]);
      }
      i = t;
    }
    }

  }//s ka end

  }
  }
}