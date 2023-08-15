#include <bits/stdc++.h>
using namespace std;
int main()
{
  // int n;
  long long n, k;
  cin >> n >> k;
  // vector<long long> a(n);
  vector<pair< int , int >> a(n);
  long long x;
  multiset<pair<int , int>> s;
  // set<pair<long long, long long>> s2;
  for (long long i = 0; i < n;i++){
    cin >> a[i].second>>a[i].first;
  }
  sort(a.begin(), a.end());
  // for (long long i = 0; i < n;i++){
  //   cout << a[i].first;
    
  // }
  long long ans=0;
  int c = 0, i = 0;
  while(i<n){
    if(s.size()==0){
      s.insert({a[i].first*-1, a[i].second});
      i++;
      continue;
    }
    auto it = s.upper_bound({a[i].second * -1, -1});
    if(it==s.end() and s.size()<k){
      s.insert({a[i].first*-1, a[i].second});
      i++;
      continue;
    }
    if(it!=s.end()){
      s.erase(it);
      s.insert({a[i].first*-1, a[i].second});
      i++;
      continue;
    }
    if(it==s.end() and s.size()>=k){
      c++;
      i++;
      continue;
    }
   

  }
  cout << n - c << endl;
    }
