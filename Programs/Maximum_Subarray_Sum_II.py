

 
def maxSubArraySum(a, size):
 
    max_so_far = -10000000000 - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0, size):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    return [start,end]
    # print("Maximum contiguous sum is %d" % (max_so_far))
    # print("Starting Index %d" % (start))
    # print("Ending Index %d" % (end))
 

no,a,b=map(int,input().split())
l=list(map(int,input().split()))
# l+=[-10000000000]
p=maxSubArraySum(l,no)
li=l[p[0]:p[1]+1]
n=len(li)
if(a<=len(li)<=b):
    print(sum(li))
    quit()
else:
    if(n<a):
        s=0
        k=[]
        for j in  range(a,b):
            for i in range(j):
                s+=l[i]
            st=0
            en=j-1
            maxy=s
            for i in range(j,no):
                s+=l[i]
                s-=l[i-a]
                # print(s)
                if(s>maxy):
                    maxy=s
                    st=i-a+1
                    en=i
            k.append(maxy)
        print(max(k))
        
        
        # print(l[st:en+1])
        while(j>1):
            if(en+1<n and st-1>=0):
                if(l[en+1]>l[st-1]):
                    maxy+=l[en+1]
                    en+=1
                    j-=1
                    
                else:
                    maxy+=l[st-1]
                    st-=1
                    j-=1
            elif(en+1<n):
                maxy+=l[en+1]
                en+=1
                j-=1  
            elif(st-1>=0):
                maxy+=l[st-1]
                st-=1
                j-=1
        print(maxy)
        # print(l[st:en+1])

                       
            
    if(n>b):
        while(n-b>0):
            if(p[0]-1>=0 and p[1]<no):
                if(li[0]<=li[n-1]):
                    li.pop(0)
                  
                    n-=1
                else:
                    li.pop()
  
                    n-=1
        print(sum(li))  
        # print(li)
            
              
    
