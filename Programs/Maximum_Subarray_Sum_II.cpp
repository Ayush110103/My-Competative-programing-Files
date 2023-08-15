#include <bits/stdc++.h>
using namespace std;
int main()
{
  // int n;
  long long n, a,b;
  cin >> n >> a>>b;
  // vector<long long> a(n);
  vector<long long> v(n);
  vector<long long> sum(n+1);
  long long k = 0;
  // map<pair<long long, long long>> d;
  // d[0]++;
  multiset<pair<long long,long long>> s;
  for (long long i = 0; i < n;i++){
    cin >> v[i];
  }
  for (long long i = 0; i < n;i++){
    k+= v[i];
    // cout << k << " ";
    
    sum[i + 1] = k;
  }
  // cout << endl;
  long long l=0;
  long long maxy=-1e18;

  for (int i = a; i <= b;i++){
    s.insert({sum[i], i});
  }

for (int i = 1;i<=n+1-a;i++){
  maxy = max(maxy, s.rbegin()->first - sum[i - 1]);
  s.erase({sum[i + a - 1], i + a - 1});
  if (i + b <= n)
  {
    s.insert({sum[i + b], i + b});
             } 
}
    cout<< maxy;
}