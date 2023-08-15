def atMostSum(arr, n, k):
    _sum = 0
    cnt = 0
    maxcnt = 0
     
    for i in range(n):
 
        # If adding current element doesn't
        # Cross limit add it to current window
        if ((_sum + arr[i]) <= k):
            _sum += arr[i]
            cnt += 1
         
        # Else, remove first element of current
        # window and add the current element
        elif (_sum != 0):
            _sum = _sum - arr[i - cnt] + arr[i]
         
        # keep track of max length.
        maxcnt = max(cnt, maxcnt)
 
    return maxcnt
     

n,t=map(int,input().split())
a=list(map(int,input().split()))

print(atMostSum(a, n, t))


