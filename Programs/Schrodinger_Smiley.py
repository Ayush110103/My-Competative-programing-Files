import sys
input = lambda: sys.stdin.readline().rstrip()

for aa in range(int(input())):
    n=int(input())
    s=(input())
    c=0
    k=0
    z=0
    for i in range(n):
        if(z==0):
            if(s[i]==":"):
                z=1
                k==0
                continue
        if(z==1):
            if(s[i]=="("):
                z=0
                k=0
                continue
            if(s[i]==")"):
                k=1
                continue
            if(s[i]==":"):
                if(k==1):
                    c+=1
                    k=0
    print(c)
                
                


        
                
