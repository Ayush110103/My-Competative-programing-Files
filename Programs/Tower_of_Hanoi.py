
n=int(input())
if(n%2==0):
        li=[[1,2],[1,3],[2,3]]
        k=[[1,2],[3,2],[1,3],[2,3]]
        if(n//2==1):
            print(len(li))
            for i in range(len(li)):
                  print(*li[i])
        else:
              print(3+4*(n//2-1))
              for i in range(len(li)):
                  print(*li[i])
              for i in range(1,n//2):
                  for j in range(len(k)):
                      print(*k[j  ])
else:
    li=[[1,3]]
    k=[[1,2],[3,2],[1,3],[2,3]]
    print(1+4*(n//2))
    for i in range(len(li)):
        print(*li[i])
    for i in range(1,n//2+1):
        for j in range(len(k)):
            print(*k[j])

     
