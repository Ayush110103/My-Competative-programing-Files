import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
# n,m=map(int,input().split())
li=list(map(int,input().split()))
c=0
# li.reverse()
d=[li[0]]

for i in range(1,n):
    if(li[i]>d[-1]):
        d.append(li[i])
    else:
        c+=1
        d=[li[i]]

print(c+1)
     
    
    