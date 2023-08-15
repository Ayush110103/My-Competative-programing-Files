# Ayush Jain
# Indian Institute of Technology Jodhpur
import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    d={}
    y={}
    for i in d:
        d[i]=0
    for i in d:
        d[i]+=1
    x=[]
    for i in d:
        x.append(i)
    x.sort()
    di=[]
    for i in range(len(x)-1):
        di.append(x[i+1]-x[i])
    f=d.copy()
    f.reverse()
    p=[0]
    su=[]
    s=0
    for i in di:
        s+=i
        p.append(s)
    s=0
    for i in f:
        s+=i
        f.append(s)
    ps=[0]
    sf=[0]
    s=0
    for i in p:
        s+=i
        ps.append(s)
    s=0
    for i in f:
        s+=i
        sf.append(s)
    
    # print(ps)

        

    # x=[]
    # e=li.copy()
    # for i in li:
    #     x.append([i+1,i])
    # li.sort()
    # f=[]
    # for i in range(n-1):
    #     f.append(li[i+1]-li[i]+1)
    # p=[0]
    # q=[0]
    # t=0
    # print(f)
    # s=0
    # for i in range(len(f)):
    #     s+=f[i]
    #     t+=f[n-2-1]
    #     p.append(s)
    #     q.append(t)
    # ans=[]
    # # p.reverse()
    # print(p)
    # print(q)
    # q.reverse()
    # v={}
    # for i in range(n-1):
    #     aa=sum(p)-p[i]
    #     bb=sum[q]-q[i]
    #     v[li[0]]=aa+bb
    # print(v)



        
        
    
        
        
        



        
        
