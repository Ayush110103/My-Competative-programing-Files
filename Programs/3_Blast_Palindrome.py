# import sys
# input = lambda: sys.stdin.readline().rstrip()

# def cou(arr, n, k):
 
#     # initialize the count
#     cnt = 0;
 
#     # making every element of arr in
#     # range 0 to k - 1
#     for i in range(n):
#         arr[i] = (arr[i] + k) % k;
 
#     # create an array hash
#     hash = [0]*k;
 
#     # store to count of element of arr
#     # in hash
#     for i in range(n):
#         hash[arr[i]] += 1;
 
#     # count the pair whose absolute
#     # difference is divisible by k
#     for i in range(k):
#         cnt += (hash[i] * (hash[i] - 1)) / 2;
 
#     # print value of count
#     # print(int(cnt));
#     return cnt

# for aa in range(int(input())):
#     n=int(input())
#     s=input()
#     if(n==1):
#         print("YES")
#         continue
#     r=s[::-1]
#     if(s==r):
#         print("YES")
#         continue
#     if(n%3==1):
#         print("YES")
#         continue
#     d={}
#     for  i in range(n):
#         if(s[i] in d):
#             d[s[i]].append(i+1)
#         else:
#             d[s[i]]=[i+1]
#     if(n%3==2):
#         f=0
#         for i in d:
#             if(cou(d[i],len(d[i]),4)>0):
#                 f=1
#                 break
#         for i in range(n-1):
#             if(s[i]==s[i+1]):
#                 f=1
#                 break
            
#         if(f==1):
#             print("YES")
#         else:
#             print("NO")
#     if(n%3==0):
#         f=0
#         for i in d:
#             if(len(d[i])>1 and d[i][len(d[i])-1]-d[i][0]>1):
#                 f=1
#                 break
#         for i in range(n-2):
#             if(s[i]==s[i+2]==s[i+1]):
#                 f=1
#                 break
#         if(f==1):
#             print("YES")
#         else:
#             print("NO")
                
