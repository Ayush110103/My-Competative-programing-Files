import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
li=list(map(int,input().split()))
li.sort()
if(n%2==0):
    k=n//2-1
else:
    k=n//2
c=0
for i in li:
    c+=abs(li[k]-i)
print(c)