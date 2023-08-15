#include <bits/stdc++.h>
using namespace std;


int lengthOfLIS(vector<long long>& nums)
{
   
    int n = nums.size();
    vector<int> ans;
    ans.push_back(nums[0]);
 
    for (int i = 1; i < n; i++) {
        if (nums[i] > ans.back()) {
            
            ans.push_back(nums[i]);
        }
        else {
           
            int low = lower_bound(ans.begin(), ans.end(),
                                  nums[i])
                      - ans.begin();
            ans[low] = nums[i];
        }
    }
 
   
    return ans.size();
}

int main()
{
  long long n;
  cin >> n;
  
  
    vector<long long> a(n);
    
    long long x;
    for (long long i = 0; i < n;i++){
      cin >> x;
      a[i] = x;
      
    }
    cout << lengthOfLIS(a)<<endl;
}

