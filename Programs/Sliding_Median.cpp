// Description: Sliding Median
#include <bits/stdc++.h>
using namespace std;
  
// Header files, namespaces,
// macros as defined above
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
int main()
{
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  ordered_set <pair<int,int>> s;
  for (int i = 0; i < n;i++){
    cin >> a[i];
    // s.insert(i);
    }
  int st=0 ;
  for (int i = 0; i < k;i++){
    s.insert({a[i],i});
  }
  int med = (k - 1) / 2;
  cout << (*s.find_by_order(med)).first << " ";
  for (int i = k ; i <n;i++){
    s.insert({a[i],i});
    s.erase({a[st],st});
    st++;
    cout << (*s.find_by_order(med)).first << " ";
  }
}