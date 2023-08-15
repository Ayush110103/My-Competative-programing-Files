for aa in range(int(input())):
   
    m,n=(map(int,input().split()))
    k=abs(m)+abs(n)
    s=""
    for i in range(m):
        s+="0 1 "
    for i in range(abs(n)):
        s+="0 -1 "
    # s+="-1"
    print(2*k)
    print(s)
    