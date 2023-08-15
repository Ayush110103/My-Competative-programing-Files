#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

vector<int> orderOfDeath(int n, int k, vector<int>& monsterHealth) {
    priority_queue<pair<int, int>> maxHeap;
    unordered_map<int, int> healthToIndex;
    vector<int> order;

    // Create the priority queue and the hash map
    for (int i = 0; i < n; ++i) {
        maxHeap.push({monsterHealth[i], i});
        healthToIndex[i] = monsterHealth[i];
    }

    while (!maxHeap.empty()) {
        int target = min(k, static_cast<int>(maxHeap.size())); // Select the k or remaining monsters

        for (int i = 0; i < target; ++i) {
            auto monster = maxHeap.top();
            maxHeap.pop();

            int health = monster.first;
            int index = monster.second;

            if (healthToIndex[index] != health) {
                // The monster's health has changed since it was extracted from the priority queue
                continue;
            }

            if (health <= 0) {
                order.push_back(index);
            } else {
                maxHeap.push({health - k, index});
                healthToIndex[index] = health - k;
            }
        }
    }

    return order;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<int> monsterHealth(n);
        for (int i = 0; i < n; ++i) {
            cin >> monsterHealth[i];
        }

        vector<int> order = orderOfDeath(n, k, monsterHealth);

        for (int idx : order) {
            cout << (idx + 1) << " "; // Adding 1 to the index to make it 1-indexed
        }
        cout << endl;
    }

    return 0;
}
