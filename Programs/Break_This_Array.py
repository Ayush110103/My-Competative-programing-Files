MOD = int(1e9 + 7)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def modular_inverse(n):
    return pow(n, MOD - 2, MOD)

def expected_sum(A, S):
    N = len(A)
    E = 0  # Expected sum
    for i in range(len(S)):
        if S[i] == 'L':
            A = A[:X]
        elif S[i] == 'R':
            A = A[X+1:]
        E += sum(A)
    average = E / len(A)
    gcd_val = gcd(E, len(A))
    numerator = E // gcd_val
    denominator = len(A) // gcd_val
    modular_inv = modular_inverse(denominator)
    result = (numerator * modular_inv) % MOD
    return result

# Example usage
A = [1, 2, 3, 4]  # Input array
S = 'LRRL'       # Operation string
K = len(S)       # Number of operations
expected_sum = expected_sum(A, S)
print(expected_sum)
