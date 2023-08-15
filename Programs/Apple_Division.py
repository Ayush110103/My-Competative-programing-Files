n = int(input())
apples = list(map(int, input().split()))

total_weight = sum(apples)

dp = [[False]*(total_weight//2 + 1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = True

for i in range(1, n+1):
    for j in range(1, total_weight//2 + 1):
        if j >= apples[i-1]:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-apples[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

min_diff = float('inf')
for j in range(total_weight//2 + 1):
    if dp[n][j]:
        diff = total_weight - 2*j
        min_diff = min(min_diff, diff)

print(min_diff)
