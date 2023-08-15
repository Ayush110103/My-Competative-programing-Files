import math
def modFact(n, p):
    if n >= p:
        return 0   
 
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p
 
    return result

def ncr(n, r, p):
    # initialize numerator
    # and denominator
    num = den = 1 
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, 
            p - 2, p)) % p

def power(x, y, p):
 
    # Initialize result
    res = 1
 
    while (y > 0):
 
        # If y is odd, multiply x with result
        if ((y & 1) != 0):
            res = res * x
 
        # y must be even now
        y = y >> 1  # y = y/2
        x = x * x  # Change x to x^2
 
    return res % p

# def nCr(n, r):
 
#     return (modFact(n) / (modFact(r)
#                 * modFact(n - r)))
 
# # Returns factorial of n
# def fact(n):
#     if n == 0:
#         return 1
#     res = 1
     
#     for i in range(2, n+1):
#         res = res * i
         
#     return res
for aa in range(int(input())):
    n=int(input())
    # li=list(map(int,input().split()))
    a=input()
    b=input()
    e=1000000007
    x=0
    y=0
    for i in range(n):
        if(a[i]==b[i]):
            x+=1
        else:
            y+=1
    if(y%2!=0):
        print(0)
        continue
    else:
        if(y==0):
            print(int(power(2,x,e)))
            continue
        
        
        w=y//2
        t=ncr(y,w,e)
        
        if(x==0):
            print(int(t)%e)
            continue
        print(int(power(2,x,e)*(t))%e)
    
