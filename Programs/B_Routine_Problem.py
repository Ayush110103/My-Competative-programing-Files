# from fractions import Fraction
# from decimal import Decimal
import fractions


a,b,c,d=map(int,input().split())
if(a/b<c/d):
    p=a*d
    q=b*c
    x=(q-p)/q
    # print(x)
    b = fractions.Fraction(q-p,q)
    print(b)
    quit()

if(a/b>c/d):
    p=b*c
    q=a*d
    x=(p/q)
    b = fractions.Fraction(q-p,q)
    print(b)
    quit()
if(a/b==c/d):
    print("0/1")

    

 