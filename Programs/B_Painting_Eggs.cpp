#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n], b[n];
    for (int i = 0; i < n;i++){
        cin >> a[i] >> b[i];
    }
    int x = 0, y = 0, z = 0;
    string s = "";
    for (int i = 0; i < n;i++){
        if(x>=y){
            if(x-y+a[i]<=500){
                s += "A";
                x += a[i];
                continue;
            }

            else if(x-y-b[i]<=500){
                s += "G";
                y += b[i];
                continue;
            }
            z = 1;
            break;
        }
        else{
        if(y-x+b[i]<=500){
            s+="G";
         y += b[i];
        continue;}

        else if (y - x - a[i] <= 500) {
        s += "A";
        x += a[i];
        continue;
        }
        z = 1;
        break;
    }

                                     
    }
    if(z==0){
    cout << s << endl;
    }
    else{
    cout << -1 << endl;
    }

    return 0;
}
