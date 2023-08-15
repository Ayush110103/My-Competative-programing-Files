import math  
# Below function will print the  
# all prime factor of given number  
def prime_factors(num):  
    li=[]
    # Using the while loop, we will print the number of two's that divide n  
    while num % 2 == 0:  
        li.append(2)  
        num = num / 2  
  
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
  
        # while i divides n , print i ad divide n  
        while num % i == 0:  
            li.append(i)
            num = num / i  
    if num > 2:  
        li.append(num) 
    return li

n=int(input())
k=prime_factors(n)

f=[n]
for i in k:
    if(n%i==0):
       f.append(int(n/i))
    n=n/i


print(*f)


