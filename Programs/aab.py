def update(res, L, R, K):
 
    # Converting the indices to
    # 0 indexing.
    L = L - 1
    R = R - 1
 
    # Saving the XOR of K from the starting
    # index in the range [L, R].
    res[L] = res[L] ^ K
    res[R + 1] = res[R + 1] ^ K
 
# Function to display the resulting array
def display(arr, res, n):
 
    for i in range(1, n):
 
        # Finding the resultant value in the
        # result array
        res[i] = res[i] ^ res[i - 1]
         
    for i in range(0, n):
 
        # Combining the effects of the updates
        # with the original array without
        # changing the initial array.
        print (arr[i] ^ res[i], end = " ")
 
# Driver code
arr = [ 2, 4, 6, 8, 10 ]
N = len(arr)
res = [0] * N
 
# Query 1
L = 1
R = 3
K = 2
update(res, L, R, K)
print(res)
display(arr, res, N)
print()
print(res)
print()
# Query 2
L = 2
R = 4
K = 3
update(res, L, R, K)
print(res)
# Query 3
display(arr, res, N)