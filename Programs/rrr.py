import math

T = int(input())

for case_number in range(1, T+1):
    N = int(input())
    block = int((math.sqrt(8*N + 1) - 1) / 2)
    letter = chr(65 + ((N - block*(block+1)//2) // block))
    print("Case #{}: {}".format(case_number, letter))