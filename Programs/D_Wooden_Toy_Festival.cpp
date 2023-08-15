#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int t;
    std::cin >> t;

    for (int testCase = 0; testCase < t; ++testCase) {
        int n;
        std::cin >> n;

        std::vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
        }

        std::sort(arr.begin(), arr.end());

        int low = 0;
        int high = 1e9;
        int ans = high;

        while (low <= high) {
            int x = (low + high) / 2;
            int count = 1;
            int maxm = arr[0];
            int minm = arr[0];

            for (int i = 1; i < n; ++i) {
                maxm = arr[i];
                if (((maxm - minm + 1) / 2) > x) {
                    count += 1;
                    minm = arr[i];
                }
            }

            bool func_result = (count <= 3);

            if (func_result) {
                ans = x;
                high = x - 1;
            } else {
                low = x + 1;
            }
        }

        std::cout << ans << std::endl;
    }

    return 0;
}
