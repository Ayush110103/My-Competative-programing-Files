import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    c=0
    z=0
    
    for i in range(n):
        if(z==0):
            if(li[i]<0):
                z=1
        if(z==1):
            if(li[i]>0):
                z=0
                c+=1
        # print(c)
    if(z==1):
        c+=1
    # print(c)
    an=0
    for i in range(n):
        an+=abs(li[i])
    print(an,c)
        

        
        
            
            