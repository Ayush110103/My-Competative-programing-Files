n=int(input())
l=list(map(int,input().split()))
k=n*(n+1)/2
print(int(k-sum(l)))