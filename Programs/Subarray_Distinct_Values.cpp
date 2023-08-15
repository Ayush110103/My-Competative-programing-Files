#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,k;
    cin>>n>>k;
    vector <int>a(n);
    for(int i=0;i<n;i++){
      cin >> a[i];
    }
    long long ans=0;
    map<long long,long long>d;
    int j = 0;
    for (int i = 0; i < n; i++)
    {
      /* code */
      while(j<n && ((int)d.size()<k || d.count(a[j])>0))
      {
        d[a[j]]++;
        j++;
      }
      ans += (j-i);
      d[a[i]]--;
      if(d[a[i]]==0)
        d.erase(a[i]);
    }

    cout << ans<<endl;
}