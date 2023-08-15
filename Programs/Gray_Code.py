import math as mt
def generateGrayarr(n):
 
    # base case
    if (n <= 0):
        return
 
   
    arr = list()

    arr.append("0")
    arr.append("1")
 
    
    i = 2
    j = 0
    while(True):
        
        if i >= 1 << n:
            break
        
        # print(arr)
       
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])
        # print(arr)
        for j in range(i):
            arr[j] = "0" + arr[j]
        # print(arr)
        
        for j in range(i, 2 * i):
            arr[j] = "1" + arr[j]
        i = i << 1
        print(i)
        print(arr)
 

    for i in range(len(arr)):
        print(arr[i])

n=int(input())
generateGrayarr(n)