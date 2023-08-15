import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
a.reverse()
a.append(0)

s=[]
for i in range(0,n+1,2):
    if(a[i]==0):
        break
    s.append(a[i]**2-a[i+1]**2)
# print(s)
x=(math.pi * sum(s))
# print(x)
s=str(x)
 
if(len(s)<=17):
    
    print(s)
    quit()
# print(s) 
for i in range(len(s)):
    if(s[i]=="."):
        break
# print(s)
# print(len(s))

if(int(s[i+10])>=5):
    print(s[:i+1]+str(int(s[i+1:i+11])+1))
else:
    print(s[:i+11])






