import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200001)



n,m=map(int,input().split())
d={}

for i in range(n):
    d[i+1]=[]
for i in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
# print(d)

h=[]
for i in range(n+1):
    h.append(0)
for i in range(1,n+1):
    if(h[i]==0):
        q1=[i]
        # print(h)
        q2=[]
        while True:
            while(q1!=[]):
                
                u=q1[0]
                q1.pop(0)
                if(h[u]==0):
                    h[u]=1
                
                    for i in d[u]:
                        if(h[i]==0):
                            q2.append(i)
                       
            # print(q2)
            if(q2==[]):
                break
            while(q2!=[]):
                u=q2[0]
                q2.pop(0)
                if(h[u]==0):
                    h[u]=2
                    for i in d[u]:
                        if(h[i]==0):
                           q1.append(i)

            if(q1==[]):
                break
h=h[1:]     
print(*h)

