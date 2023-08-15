import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    s=input()
    d=[]
    k=s[0:2]
    d.append(k)
    for i in range(2,n):
        if(s[i-1]+s[i] not in d):
          d.append(s[i-1]+s[i])
    # print(d)
    print(len(d))