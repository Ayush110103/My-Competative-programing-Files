import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
li=list(map(int,input().split()))
c=0
d={}
for i in range(n):
    d[li[i]]=i
li.sort()
for i in range(n-1):
    if(d[li[i+1]]-d[li[i]]<0):
        c+=1

print(c+1)
        
