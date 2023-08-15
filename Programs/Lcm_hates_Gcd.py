# cook your dish here
import math
for aa in range(int(input())):
    a,b=(map(int,input().split()))
    li=[]
    print(min((a*a)//math.gcd(a,a)-math.gcd(a,b),(b*a)//math.gcd(b,a)-math.gcd(b,b)))

    