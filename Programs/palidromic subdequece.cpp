
#include <bits/stdc++.h>
using namespace std;
int main()
{
  string s;
  cin >> s;
  int n = s.length();
  string t = s;
  reverse(t.begin(), t.end());
  // vector<string> d;
  if(s==t){
    // return s;
    cout << s;
    
  }
  string a (1,s[0]), b (1,t[n-1]);
  // cout << a << " " << b << endl;
  int rem = -1;
  for (int  i = 1; i < n-1; i++)
  {
    /* code */
    a = t[n - 1 - i] + a;
    b= b + s[i];
    cout << a << " " << b << endl;
    if(a==b){
      rem = i;
    }
    }
    rem++;
    string ad;
    cout << rem;
    if(rem==0){
    ad= t.substr(0,n-1);
    }
    else{
      ad = t.substr(0,n-rem);
    }
    cout << ad+s;
  }


