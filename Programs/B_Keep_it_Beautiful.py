import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    # n,m=map(int,input().split())
    li=list(map(int,input().split()))
    s="1"
    st=li[0]
    l=li[0]
    mini=li[0]
    z=0
    for i in range(1,n):
        if(z==0):
          if(li[i]>=l):
              s+="1"
              l=li[i]
              continue
            # print(li[i])
          if(st>=li[i]):
              s+="1"
              l=li[i]
              z=1
              continue
        if(z==1):
          if(st>=li[i] and li[i]>=l):
              s+="1"
              l=li[i]
              
              continue
            # print(li[i])
        
        s+="0"
        # print(li[i])
           
    print(s)
            



        