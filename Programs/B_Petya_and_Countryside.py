def lenOfLongIncSubArr(arr, n) :
 
    
    m = 1
    l = 1
    z=0
    i=1
    # traverse the array from the 2nd element
    while(i<n):

        if(z==1):
            if (arr[i] <= arr[i-1]) :
                 l =l + 1
                 i+=1
            else:
                if (m < l)  :
                   m = l
                l=1
                z=0
                i=r+1
                continue
 
            
            
            



        if(z==0):
            if (arr[i] >= arr[i-1]) :
                l =l + 1
                i+=1
                continue
            else:
                z=1
                l+=1
                r=i
                i+=1

                continue
 
            
            
         
         
   
    if (m < l) :
        m = l
      
   
    return m


n=int(input())
li=list(map(int,input().split()))
if(n==1):
    print(1)
    quit()
print(lenOfLongIncSubArr(li,n))
