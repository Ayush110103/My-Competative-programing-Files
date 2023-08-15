#include <iostream>
using namespace std;
  
// Header files, namespaces,
// macros as defined above
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
  
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
int main(){
  int n, k;
  cin >> n >> k;
  ordered_set s;
  for (int i = 1; i <= n;i++){
    s.insert(i);
    }
  int st=0 ;
  while(s.size()>1){
    st = (st + k) % s.size();

    auto it = s.find_by_order(st);
    cout << *it << " ";
    s.erase(it);
    }
  cout << *s.begin() << endl;
  return 0;



    }