
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while(t--){
  int n;
  cin >> n;
  vector<int> v(n);
  vector<priority_queue<pair<int, int>>> pq(n + 1);
  for (int i = 0; i < n; i++)
  {
    cin>>v[i];
    v[i]--;
}

vector<int>dp(n+1,0);
for(int i=0;i<n;i++){
    dp[i+1]=dp[i];
    if(!pq[v[i]].empty()){
        int j=pq[v[i]].top().second;
        dp[i+1]=max(dp[i+1],dp[j]-j+i+1);
    }
    pq[v[i]].push({dp[i]-i,i});
}
cout<<dp[n]<<endl;}
}

