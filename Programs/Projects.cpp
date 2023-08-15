#include <bits/stdc++.h>
using namespace std;
#include<tuple> 


struct pro{
  long long s, e, r;
};
bool cmp(pro &p1,pro &p2){
  return p1.e < p2.e;
}
long long find_best(vector<long long>&ep,long long v){
  auto it = lower_bound(ep.begin(), ep.end(),v);
  if(it==ep.begin()){
    return 0;
  }
  else{
    it--;
    return 1+distance(ep.begin(),it);
  }
}

int main()
{
  long long  n;
  cin >> n;
  
  vector<pro> v(n+1);
  vector<long long> ep;
  // cout << 1;

  for (long long i = 1; i <n+1; i++)
  {
    cin >> v[i].s >> v[i].e >> v[i].r;
    // cout << v[i].s << " "; 
    }
  
  sort(v.begin(),v.end(),cmp);
  
  for (long long i = 1;i<=n;i++){
    ep.push_back(v[i].e);
  }
  // cout << ep[0]<<ep[1]<<ep[2]<<ep[3];
  vector<long long>dp(n+1,0);
  dp[0] = 0;
  for(long long i=1;i<=n;i++){
    dp[i] = max(dp[i-1],v[i].r+dp[find_best(ep,v[i].s)]);
    // cout << dp[i]<< endl;
    // cout <<v[i].r+dp[find_best(ep,v[i].s)] << endl;

  }
  cout << dp[n]<<endl;
  return 0;
}
