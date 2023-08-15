for i in range(int(input())):
    n = int(input())
    s = -1
    for i in range(1,n+1):
        tempy = 0
        maxy = -1
        idx = 1
        for j in range(n-i):
            tempy += (j+1)*idx
            maxy = max((j+1)*idx,maxy)
            idx+=1
 
        for j in range(n,n-i,-1):
            tempy += idx*j
            maxy = max(idx*j,maxy)
            idx+=1
        s = max(s,tempy-maxy)
        # print()
 
    print(s)