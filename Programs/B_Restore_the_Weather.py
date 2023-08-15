for _ in range(int(input())):
    n, k = map(int, input().split())

    li = list(map(int, input().split()))
    b = list(map(int, input().split()))
    create=[]
 
    for i in range(n):
        create.append((li[i],i))
    p=[]
    for i in range(n):
        if(li[i]>0):
            p.append(li[i])
      
    create.sort()

    b.sort()
    final_arr = [0] * n
    if(p!=[]):
       p.sort()

    for i in range(n):
        final_arr[create[i][1]] = b[i]
    if(p!=[]):
        p.reverse()
    print(*final_arr)