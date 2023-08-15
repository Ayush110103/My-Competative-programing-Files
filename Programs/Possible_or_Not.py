import math

t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    b_count = []
    bit_arr = [0] * 30
    
    for i in range(n):
        if (arr[i] & k) == k and arr[i] >= k:
            b_count.append(arr[i])
    f=0
    for i  in range(n):
        f=f&k
    if len(b_count) >= 2:
        for i in range(len(b_count)):
            for j in range(30):
                power = int(math.pow(2, j))
                element = b_count[i] - k
                if (element & power) == 0:
                    bit_arr[j] = 1
        
        sum = 0
        for i in range(30):
            if bit_arr[i] == 1:
                sum += 1
        
        if sum == 30:
            print("YES")
        else:
            print("NO")
    elif len(b_count) == 1:
        if b_count[0] == k:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    
    t -= 1
