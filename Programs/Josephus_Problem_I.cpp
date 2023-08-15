
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  if(n==1){
    cout << 1 << endl;
    return 0;
  }
  set<int> s;
  for (int i = 1; i <= n;i++){
    s.insert(i);
  }
  // for (auto i = s.begin(); i !=s.end();i++){
  //   cout << *i << " ";
  // }
  int i = 2;
  auto it = s.begin();

  // cout << *it;
  it++;
  // cout << *it;
  while(s.size()>1){
    if(i%2==0){
      cout << *it << " ";
      it = s.erase(it);
      if(it==s.end()){
        it = s.begin();
      }

    }
    else{
      it++;
      if(it==s.end()){
        it = s.begin();
      }
    }
    i++;
  }
  cout << *s.begin() << endl;
}

