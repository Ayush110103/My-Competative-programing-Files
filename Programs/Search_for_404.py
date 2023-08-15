# Created by iN_siDious.
# Copyright © 2023 iN_siDious. All rights reserved.
import sys
import random
# from math import *
from string import ascii_lowercase
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
from heapq import heappushpop, heapify, heappop, heappush
from bisect import bisect_left,bisect_right
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
inp = lambda: sys.stdin.buffer.readline().decode().strip()
out=sys.stdout.write
def Query(i):
    print("?", i, flush=True)
    qi=int(inp())
    return qi
def S():
    return inp()
def I():
    return int(inp())
def MI():
    return map(int, inp().split())
def MS():
    return inp().split()
def LS():
    return list(inp().split())
def LI():
    return list(map(int,inp().split()))
def print1(x):
    return out(str(x)+"\n")
def print2(x,y):
    return out(str(x)+" "+str(y)+"\n")
def print3(x,y,z):
    return out(str(x)+" "+str(y)+" "+str(z)+"\n")
def print_arr(arr):
    for num in arr:
        out(str(num)+" ")
    out(str("\n"))
mod=10**9+7
for _ in range(I()):
    n=I()
    ss=S()
    fours,zeros,stars=ss.count("4"),ss.count("0"),ss.count("*")
    f,z,s=0,0,0
    ans=0
    for i in range(n):
        rf,rz,rs=fours-f,zeros-z,stars-s
        if ss[i] in ("0","*"):
            if ss[i]=="*": rs-=1
            l=(f*(pow(2,max(0,s),mod))+(s*pow(2,max(0,s-1),mod)))%mod
            r=(rf*(pow(2,max(0,rs),mod))+(rs*pow(2,max(0,rs-1),mod)))%mod
            # print(f,s,rf,rs,l,r)
            ans+=(l*r)%mod
            ans%=mod
        if ss[i]=="4": f+=1
        elif ss[i]=="0": z+=1
        else: s+=1
    print1(ans%mod)
            
    

            
            
        
        
    
    