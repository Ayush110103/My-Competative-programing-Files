#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  int a[n];
  for (int i = 0; i < n;i++){
    int x;
    cin >> x;
    a[i] = x;

  }
    multiset<int> tower;
    for (int i = 0; i < n; i++)
    {   if(tower.size()==0){
      tower.insert(a[i]);
      continue;
    }
      auto it = tower.upper_bound(a[i]);
        if (it == tower.end())
            tower.insert(a[i]);
        else
        {
            tower.erase(it);
            tower.insert(a[i]);
        }
    }
    cout << tower.size() << endl;
    return 0;
}