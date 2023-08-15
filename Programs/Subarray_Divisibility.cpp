#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
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
        if(r>=0)
          t=abs(r)%n;
        else
          t=(n-abs(r)%n)%n;
        // cout << t<<" ";
        c+=d[abs(t)];
        // cout<<c;
        d[abs(t)]++;
    }
    cout<<c<<endl;
}