# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    d={}
    li.sort()
    for i in li:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    z=0
    for i in d:
        if(d[i]>n//2):
            z=1
            break
    if(z==1):
        k=n//2
        o=0
        f=sum(li)
        i=1
        j=0
        while True:
            t=i*k
            if(t<=f):
                if(f>i):
                    o=1
                    break
                else:
                    o=2
                    break
            f-=t
            j+=k
            if(j>n):
                o=1
                break
            i+=1
        if(o==1):
            print("NO")
        elif (o == 2 and sum([x-y for x, y in zip(  
                li[:k], li[n-k:])]) == 0):
                print("NO") 
        else :
              


                

            
            
                
    else:
        print("YES")

            