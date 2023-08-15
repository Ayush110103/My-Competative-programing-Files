# cook your dish here
for aa in range(int(input())):
    n=int(input())
    if(n==1):
        print(-1)
        continue
    li=[]
    
    for i in range(2,int(n**(0.5))+2):
        if(n%i==0):
            r=i
            break
    k=n//r
    if(k==1 or k==r):
        print(-1)
        continue
    
    
    print(1,int(k),int(r))
    
    


