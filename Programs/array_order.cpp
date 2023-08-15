
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  
  vector<int> a(n);
  int d;
  for (int i = 0; i < n;i++){
    cin >> d;
    a[i] = d;

  }
  vector<pair<int, int>> x;
  vector<pair<int, int>> y;

  for (int i = 0; i < n;i++){
    if(a[i]<0){
      pair<int, int> p(i, a[i]);
      y.push_back(p);
      }
    else{
      pair<int, int> p(i, a[i]);
      x.push_back(p); 
    }
}
sort(x.begin(), x.end());
sort(y.begin(), y.end());
for (int i = 0; i < y.size();i++){
  cout <<y[i].second<<" ";
}
for (int i = 0; i < x.size();i++){
  cout << x[i].second << " " ;
}

}

    