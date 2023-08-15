#include <bits/stdc++.h>
using namespace std;
int main()
{
  // int n;
  long long n, k;
  cin >> n >> k;
  vector<long long> a(n);
  vector<pair<long long,long long>> b(k);
  long long x;
  set<pair<long long, long long>> s1;
  set<pair<long long, long long>> s2;
  for (long long i = 0; i < n;i++){
    cin >> a[i];
  }
  if(k==1){
    for (long long i = 0; i < n; i++)
    {
      /* code */
      cout << 0 << " ";
    }
    return 0;
  }
  if(k==2){
    for (long long i = 0; i < n-1; i++)
    {
      /* code */
      cout << abs(a[i]-a[i+1]) << " ";
    }
    return 0;
  }
  long long t = int((k - 1) / 2);
  // cout << t;
  for (long long i = 0; i < k; i++)
  {
    /* code */
    b[i]={a[i], i};
  }

  sort(b.begin(), b.end());
  // for (long long i = 0; i < k; i++)
  // {
  //   /* code */
  //   cout << b[i].first;
  // }
  long long p = 0, q = 0;
  for (long long i = 0; i <= t;i++){
    s1.insert({b[i].first, b[i].second});
    p += b[i].first;
    // cout << p << b[i].first;
  }
  // cout << p;
  for (long long i = t + 1; i < k;i++){
    s2.insert({b[i].first, b[i].second});
    q += b[i].first;
  }
  // cout << p << q;
  long long m = s1.rbegin()->first;
  cout << m * s1.size() - p + q - m * s2.size()<<" ";
  for (long long i = k; i < n; i++)
  {
    if(s1.count({a[i - k], i - k})){
        s1.erase({a[i - k], i - k});
        p -= a[i - k];
    }
    else{
    s2.erase({a[i - k], i - k});
    q -= a[i - k];
    }
    long long r = s1.rbegin()->first;
    if(r>=a[i]){
      s1.insert({a[i], i});
      p += a[i];
    }
    else{
        s2.insert({a[i], i});
        q += a[i];
    }
    while(s1.size()<k/2+k%2){
        s1.insert(*s2.begin());
        p += s2.begin()->first;
        q -= s2.begin()->first;
        s2.erase(s2.begin());
    
    }
    while(s1.size()>k/2+k%2){
        s2.insert(*s1.rbegin());
        q += s1.rbegin()->first;
         p -= s1.rbegin()->first;
        s1.erase(*s1.rbegin());
       
    }

    m = s1.rbegin()->first;
    cout << s1.size() * m - p + q - s2.size() * m<<" ";
  }
}