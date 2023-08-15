for aa in range(int(input())):
    
    a,b=(map(int,input().split()))
    k=abs(a)
    t=abs(b)
    if(k==t):
        print(2*(k))
        continue
    print(2*min(k,t)+2*(max(k,t)-min(k,t))-1)