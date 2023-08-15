# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    x=[]
    a=[]
    b=[]
    for i in range(n):
         k=int(input())
         li=list(map(int,input().split()))
        #  print(li)
         a.append(min(li))
         li.remove(min(li))
         b.append(min(li))
    # print(a)
    # print(b)
    ans=min(a)
    b.sort()
    b.reverse()
    b=b[:n-1]
    ans+=sum(b)
    print(ans)
    



    
         