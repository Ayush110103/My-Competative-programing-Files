import sys
input = lambda: sys.stdin.readline().rstrip()


n=int(input())

li=list(map(int,input().split()))
max=-10000000000
sum=0
for i in range(n):
    sum+=li[i]
    if(sum>max):
        max=sum
    if(sum<0):
        sum=0
print(max)
