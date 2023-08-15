def find_X(A, B, C):
    # Find the bits where A, B, and C differ
    D = (A^B) | (A^C) | (B^C)
    # Choose the initial lower and upper bounds for X
    lo = 0
    hi = (1<<30)-1
    # Binary search for the value of X that satisfies the conditions
    while lo < hi:
        mid = (lo + hi) // 2
        if (A^mid) < (B^mid) and (B^mid) < (C^mid) and (A^mid) < (C^mid):
            hi = mid
        else:
            lo = mid + 1
    # Check if the final value of X satisfies the conditions
    if (A^lo) < (B^lo) and (B^lo) < (C^lo) and (A^lo) < (C^lo):
        return lo
    else:
        return -1
for i in range(int(input())):    
    # n=int(input())
    a,b,c=map(int,input().split())
    print(find_X(a,b,c))