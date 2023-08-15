for aa in range(int(input())):
    n,k=map(int,input().split())
    if(k<1-n or  k>n+1):
            print(-1)
            continue
       
    
    s=""
    v=1
    if(k>=1):
        while(v!=k):
                v+=1
                s+="+"
        for i in range(n-k+1):
              s+="*"
    if(k<1):
            while(v!=k):
                v-=1;
                s+="-"
            for i in range(n-abs(k)-1):
                 s+="*"   
    print(s)
    
        



    