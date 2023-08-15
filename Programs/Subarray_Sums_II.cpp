#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,s;
    cin>>n>>s;
    vector<long long> v(n);
    vector<int> a(n);
    for (int i=0;i<n;i++){
        cin>>v[i];
    }
    
    
    map<long long,long long> d;
    d[0]++;
    long long r=0,c=0;
    long long t;
    for (int i=0;i<n;i++){
        r+=v[i];
        c+=d[r-s];
        // cout<<c;
        d[r]++;
    }
    cout<<c<<endl;
}