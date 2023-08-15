import math
 
# Recursive Implementation
def GcdOfArray(arr, idx):
    if idx == len(arr)-1:
        return arr[idx]
       
    a = arr[idx]
    b = GcdOfArray(arr,idx+1)
     
    return math.gcd(a, b)

for aa in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    d={}
    z=0
    li.sort()
    for i in li:
        if(i not in d):
            d[i]=1
        else:
            z=1
            break
    if(z==1):
        print("NO")
        continue
    li.sort()
    

    e=[]
    o=[]
    for i in li:
        if(i%2==0):
            e.append(i)
        else:
            o.append(i)
    if(len(o)>len(e)):
        if(len(e)>1):
            print("NO")
            continue
        else:
            print("YES")
            continue
    if(len(o)<len(e)):
        if(len(o)>1 ):
            print("NO")
            continue
        else:
            print("YES")
            continue
    if(len(e)==len(o)==1):
        print("YES")
        continue
    if(len(o)==len(e)):
        print("NO")
        continue





    