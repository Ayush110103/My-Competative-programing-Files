
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
 int x, y;
  
  vector<pair<pair<int,int>,int>> cus;
  for (int i = 0; i < n;i++){
    cin >> cus[i].first.first>> cus[i].first.second;
    cus[i].second = i;
  }
  sort(cus.begin(), cus.end());
  vector<int> ans(n);
  int r_id = 1;
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> p;
  for (int i = 0; i < n; i++)
  {
    /* code */
    if(p.size()==0){
      p.push({cus[i].first.second, r_id});
      ans[cus[i].second] = r_id;
      r_id++;
    }
    else{
      pair<int, int> x = p.top();
      if(x.first < cus[i].first.first){
        p.pop();
        p.push({cus[i].first.second, x.second});
        ans[cus[i].second] = x.second;
      }
      else{
        p.push({cus[i].first.second, r_id});
        ans[cus[i].second] = r_id;
        r_id++;
      }

    }
  }
  cout << r_id - 1 << endl;
  for (int i = 0; i < n; i++)
  {
    /* code */
    cout << ans[i] << " ";
  }
  


  return 0;
}
