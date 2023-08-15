#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int n = s.length();
    // cout << s[1]<< endl;

    int x = 0, y = 0;
    for (int i = 0; i < n;i++){
        int res = s[i].compare("4");
        if(res== 0){
            x += 1;
        }
        int res = s[i].compare("7");
        if(res==0){
            y += 1;
        }   
    }
    if(x==0 && y==0 ){
        cout << -1 << endl;
        return 0;
    }
    else if(x>=y){
        cout << 4 << endl;
    }
    else if(y>x){
        cout << 7 << endl;
    }
    
    return 0;
}
