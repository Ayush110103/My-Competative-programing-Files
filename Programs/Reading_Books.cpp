
#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main(){

int n;
cin>>n;
vector <long long> a(n);
long long sum=0,t1=0,t2=0;

for(int i=0;i<n;i++){
  cin >> a[i];
  sum+=a[i];
}
if(n==1){
  cout<<sum<<endl;
  return 0;
}
sort(a.begin(),a.end());

int i=0,j=n-1;
while(i<j){
     if(t1+a[i]<=t2+a[j]){
       t1 += a[i];
       i++;
     }
      else{
       t2 += a[j];
       j--;
      }    
}
t2 += a[j]; 

cout<<sum +(abs(t2-t1))<<endl;
}