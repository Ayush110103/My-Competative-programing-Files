import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())
li=list(map(int,input().split()))
li.sort()
s=1

for i in range(n):
    if(s>=li[i]):
        s+=li[i]
print(s)
    