def maxSum(n,l):
    




n=int(input())
li=list(map(int,input().split()))
d={}
li.sort()
for i in li:
    if(i in d):
        d[i]+=i
    else:
        d[i]=i
x=[]
y=[]
for i in d:
    x.append(i)
    y.append(d[i])
