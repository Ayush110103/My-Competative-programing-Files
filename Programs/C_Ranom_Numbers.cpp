#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    int aa;
    cin >> aa;
    
    for (int aa_index = 0; aa_index < aa; aa_index++) {
        string s;
        cin >> s;
        
        int r = -1;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != 'E') {
                r = i;
                break;
            }
        }
        
        if (r != -1) {
            s[r] = 'E';
        }
        
        ordered_map<char, vector<int>> d;
        for (int i = 0; i < s.length(); i++) {
            if (d.find(s[i]) != d.end()) {
                d[s[i]].push_back(i);
            } else {
                d[s[i]] = vector<int>{i};
            }
        }
        
        // Print the updated string and the map
        // cout << s << endl;
        // for (auto entry : d) {
        //     cout << entry.first << ": ";
        //     for (int index : entry.second) {
        //         cout << index << " ";
        //     }
        //     cout << endl;
        // }
    }
    
    return 0;
}
