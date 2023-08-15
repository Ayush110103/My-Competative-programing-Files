
#include <bits/stdc++.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
  // int n;
  // cin >> n;
  long long n, m;
  cin >> n >> m;
  vector<long long> a(n);
  long long x;
  for (int i = 0; i < m;i++){
    cin >> x;
    a[i] = x;
    
  }
 
  multiset<long long> k;
  priority_queue<int> pq;
  k.insert(0);
  k.insert(n);
  pq.push(n);
  for (int i = 0; i < m;i++){
    auto it = k.lower_bound(a[i]);
    if(it==k.begin()){
      it++;
      cout << pq.top();
      continue;
    }
    

  }
  
}
