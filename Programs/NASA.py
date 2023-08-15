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

def is_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    d={}
    t=[]
    c=0
    for i in li:
          if i in d:
              d[i]+=1

          else:
              d[i]=1
    r=[]
    # print(d)
    for i in d:
        if(d[i]>=2):
          c+=nCr(d[i],2)+d[i]
        else:
            c+=1
        r.append(i)
    if(len(d))<=1:
        print(int(c))
        continue
    for i in range(len(d)):
        for j in range(i):
            p=r[i]^r[j]
            if(is_palindrome(p)):
                c+=1
    # print(r)
    # print(d)
    print(c)

    

        
    
        
    
    
              
  
    
    

    

        
        
        