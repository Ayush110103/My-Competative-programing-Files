import sys
input = lambda: sys.stdin.readline().rstrip()
mod= 10**9+7
for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    li.reverse()
    x=li[0]
    y=0
    for i in range(n):
        y+=1
    c=1
    for i in range(len(li)):
        if x<li[i]:
            c+=1
            x=li[i]
        else:
            if i!=0:
                x=x^li[i]      
    print(c)