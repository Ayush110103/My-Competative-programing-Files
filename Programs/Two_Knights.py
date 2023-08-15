

n=int(input())
if(n==1):
    print(0)
    quit()
if(n==2):
    print(0)
    print(6)
    quit()
print(0)
print(6)
for i in  range(3,n+1):
    u=i**2
    t=int((u-3*i+2)/2)
    # li.append(int(nCr(i**2,2))-8*t)
    print(int(u*(u-1)/2)-8*t)
