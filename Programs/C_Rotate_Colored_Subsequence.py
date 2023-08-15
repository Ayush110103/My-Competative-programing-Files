# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()


n,m=map(int,input().split())
s=input()
d={}
li=list(map(int,input().split()))
for i in range(n):
    if(li[i] in d):
        d[li[i]].append(i)
    else:
        d[li[i]]=[i]
a=[""]*n
for i in range(m):
    if(len(d[i+1])==1):
        a[d[i+1][0]]=s[d[i+1][0]]
        continue
    t=len(d[i+1])
    f=d[i+1]
    u=s[f[t-1]]
    for j in range(t-1):
        a[f[t-1-j]]=s[f[t-2-j]]
    a[f[0]]=u
h=""
for i in range(n):
    h+=a[i]
print(h)


        
        
        
    
