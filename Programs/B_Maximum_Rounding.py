# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    s=str(n)
    k=s
    s=s[::-1]
    li=list(map(int,s))
    li=li+[0]
    # print(li)
    z=0

    for i in range(len(li)-1):
        if(li[i]>=5):
            z=1
            li[i+1]+=1
    if(z==0):
        print(n)
        continue
    li.reverse()
    for i in range(len(li)):
        if(li[i]>=5):
            r=i
            break
    t=""
    for i in range(r):
        if(i==0):
            if(li[0]==0):
                continue
        t+=str(li[i])
    for i in range(r,len(li)):
        t+="0"
    
    print(t)
        
    
        

