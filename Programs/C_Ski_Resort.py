import sys
input = lambda: sys.stdin.readline().rstrip()

def nCr(n, r):
 
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
# Returns factorial of n
def fact(n):
    if n == 0:
        return 1
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res

for aa in range(int(input())):
    # n=int(input())
    n,m,q=map(int,input().split())
    li=list(map(int,input().split()))
    t=[]
    c=0
    for i in range(n):
        if(li[i]<=q):
            c+=1
        else:
            t.append(c)
            c=0
    t.append(c)
    l=0
    # print(t)
    for  i in range(len(t)):
        if(t[i]>=m):
            f=t[i]-m+1
            l+=int(f*t[i]-((f/2)*(2*(m)+(f-1)))+f)
    print(l)
        

        