def best_maximum_waiting_time(n, toy_patterns):
    low = 0
    high = max(toy_patterns) - min(toy_patterns)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        feasible = False

        for i in range(n - 1):
            if toy_patterns[i + 1] - toy_patterns[i] > 2 * mid:
                feasible = True
                break

        if feasible:
            low = mid + 1
        else:
            result = mid
            high = mid - 1

    return result

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    toy_patterns = list(map(int, input().split()))
    result = best_maximum_waiting_time(n, toy_patterns)
    print(result)
