import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    s=input()
    t=s[0]
    a=""
    for i in range(1,n-1):
        if(t==""):
            t=s[i]
            continue
            
        
        if(s[i]==t):
            a+=s[i]
            t=""
            
            # print(a)
        
    a+=t
    print(a)
        
