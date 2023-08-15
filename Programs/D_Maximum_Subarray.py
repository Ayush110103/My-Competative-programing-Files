from sys import maxint
def nixi(a, size):
  
    max_so_far = -maxint - 1
    max_ending_here = 0
  
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
  
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

for aa in range(int(input())):
    n,k,x=map(int,input().split())
    li=list(map(int,input().split()))
    max_so_far = -maxint - 1
    max_ending_here = 0
  
    for i in range(0,n):
        max_ending_here = max_ending_here + li[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            
  
        if max_ending_here < 0:
            max_ending_here = 0



  
     