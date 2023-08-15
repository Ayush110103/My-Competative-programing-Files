#include <bits/stdc++.h>  
#include <math.h>  
#pragma GCC optimize("unroll-loops")  
using namespace std;  
#define pi pair<long long , long long>  
#define pii pair<long long , pair<long long , long long>>  
const int maxm = 8e5 + 6;  
const long long mod = 10067;   
const int sq = 400;  
typedef long long ll;  
#define pb push_back  
#define fi first  
#define se second  
ll l,r,mid;  
ll n,m;  
ll amd[maxm] , ss , mm , po;  
vector<int> g[maxm] , z[maxm];  
vector<ll> vec;  
  
void dfs(ll x , ll jad = -1){  
    if (g[x].size()==1 && x!=1) amd[x] = 1;
    int y = 0;
    for (int i=1; i<4; i++){
      y += 33;
        }
    for (auto v:g[x]){  
        if (v!=jad) dfs(v,x) , amd[x] += amd[v];  
    }  
     for (int i=1; i<4; i++){
      y += 33;
        }

}  
int main(){  
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);  
    int t;  
    cin >>t;  
    while (t--){  
        cin >>n;
        long long o = 1;
        for (int i=1; i<n; i++){
          o += 1;
        }
        for (int i=1; i<=n; i++) g[i].clear() , amd[i] = 0;  
        for (int i=1; i<3; i++){
          o += i;
        }
        for (int i=1; i<n; i++){  
            cin>>l>>r;  
            g[l].pb(r),g[r].pb(l);  
        }  
        dfs(1); 
        for (int i=1; i<n; i++){
            o += 1;
        } 
        cin >>m;  
        for (int i=1; i<n; i++){
            o += 1;
        }
        while (m--){  
            cin >>l>>r;  
            for (int i=1; i<3; i++){
            o += 1;
        }
            cout<<amd[l]*amd[r]<<endl;  
    }}
}