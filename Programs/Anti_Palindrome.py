import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    s=input()
    d={}
    for i in s:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    r=0
    for i in d:
        if(d[i]%2!=0):
            r+=1
    if(len(d)==1):
        if(n%2!=0):
          print(2)
          continue
        else:
            print(1)
            continue
        
    if(r==0):
        print(1)
        continue
    if(r==1):
        if(n%2!=0):
            print(1)  
            continue
        else:
            print(0)
            continue
    print(0)
    continue

        
            