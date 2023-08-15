#include <iostream>
#include <vector>
using namespace std;

int main() {
    int aa;
    cin >> aa;
    
    for (int aa_index = 0; aa_index < aa; aa_index++) {
        int n;
        cin >> n;
        
        vector<int> li(n);
        for (int i = 0; i < n; i++) {
            cin >> li[i];
        }
        
        string s = "1";
        int st = li[0];
        int l = li[0];
        int z = 0;
      
        for (int i = 1; i < n; i++) {
          
            if (z == 0) {
                if (li[i] >= l) {
                    s += "1";
                    l = li[i];
                    continue;
                }
                
                if (st >= li[i]) {
                    s += "1";
                    l = li[i];
                    z = 1;
                    continue;
                }
            }
            
            if (z == 1) {
                if (st >= li[i] && li[i] >= l) {
                    s += "1";
                    l = li[i];
                    continue;
                }
            }
            
            s += "0";
        }
        
        cout << s << endl;
    }
    
    return 0;
}
