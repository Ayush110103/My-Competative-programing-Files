
#include <bits/stdc++.h>
#include <iostream>  

#include <string>  
using namespace std;
int main()
{
  int n;
  cin >> n;
  string k = to_string(n);
  set<int> a;
  long long c = 0;
 

 
  while(n!=0){
  for (int i = 0; i < k.length(); i++)
  {
    // cout << k[i];
    int f = k[i]-'0';
    a.insert(f);
  }
  auto it = a.rbegin();
  n = n - *it;
  k = to_string(n);
  a = {};
  c++;
  }
  cout << c<< endl;
}
