

def lps(s):
      
    n = len(s)
  
    # a[i] is going to store length
    # of longest palindromic subsequence
    # of substring s[0..i]
    a = [0] * n
  
    # Pick starting point
    for i in range(n-1, -1, -1):
  
        back_up = 0
  
    # Pick ending points and see if s[i]
    # increases length of longest common
    # subsequence ending with s[j].
        for j in range(i, n):
  
    # similar to 2D array L[i][j] == 1
    # i.e., handling substrings of length
    # one.
            if j == i: 
                a[j] = 1 
  
    # Similar to 2D array L[i][j] = L[i+1][j-1]+2
    # i.e., handling case when corner characters
    # are same. 
            elif s[i] == s[j]:
                temp = a[j]
                a[j] = back_up + 2
                back_up = temp
  
    # similar to 2D array L[i][j] = max(L[i][j-1],
    # a[i+1][j])
            else:
                back_up = a[j]
                a[j] = max(a[j - 1], a[j])
  
    return a[n - 1]
# Driver Code


for aa in range(int(input())):
    n=int(input())

    s=input()
    
        

    # a=list(map(int,input().split()))
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    a=""
    for i in s:
        if(d[i]>1):
            a+=i
    # print(a)
    s=a[:]
    n=len(s)
    if(n==0):
        print(0)
        continue
    if(n<=3):
        print(1)
        continue
    k=s[::-1]
    x=[]
    u=lps(s)
    print(u//2)
    

    # for i in range(n):
    #     if(d[s[i]]==2):
    #         x.append(i)
    #         d[s[i]]-=1
    #     else:
    #         d[s[i]]-=1
    # # print(max(x))
    # # print(k)
    # m=0
    # r=[]
    # t=[]

    # for i in  range(2,max(x)+2):
    #     r.append(s[:i])
    #     t.append(k[:n-i])


    # for i in  range(len(r)):
    #     # print(s[:i] , k[:n-i])
    #     m=max(m,lcs(r[i] , t[i]))
    # print(m)