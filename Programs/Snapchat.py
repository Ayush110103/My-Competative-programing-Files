# cook your dish here
# cook your dish here
for aa in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    max=0
    for i in range(n):
        
        if(a[i]==0 or b[i]==0):
            if(max<c):
                max=c
            c=0
        else:
            c+=1
    if(c>max):
        max=c
    print(max)