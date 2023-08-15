/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    vector <pair<long long,long long>> a(n);
    long long ans=0;
    for(int i=0;i<n;i++){
        cin>>a[i].first>>a[i].second;
        ans+=a[i].second;
    }
    sort(a.begin(),a.end());
    // for(int i=0;i<n;i++){
    //     cout << a[i].first;
    // }
    
    for (int i=0;i<n;i++){
        ans-=(n-i)*(a[i].first);
    }
    cout<<ans<<endl;
    
    
}
