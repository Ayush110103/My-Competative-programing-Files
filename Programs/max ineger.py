n, k = input().split()
k = int(k)

while k > 0:
    max_digit = min(n)
    n = n.replace(max_digit, '', 1)
    k -= 1

print(int(n))