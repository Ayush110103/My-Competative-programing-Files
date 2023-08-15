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
    int n,s;
    cin>>n>>s;
    vector <pair<int,int>>a(n);
    for(int i=0;i<n;i++){
        cin>>a[i].first;
        a[i].second=i+1;
        
    }
    sort(a.begin(),a.end());
    for (int i=0;i<n-2;i++){
        int x=s-a[i].first;
        int k=n-1;
        for (int j=i+1;j<n-1;j++){
            while(a[j].first+a[k].first > x)
                k--; 
            if(j<k && a[j].first+a[k].first == x){
                    cout<<a[i].second<<" "<<a[j].second<<" "<< a[k].second;
                    return 0;
                
            }
            
        }
    }
    cout<<"IMPOSSIBLE";
    
    
}
