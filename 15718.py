import math
import sys
from functools import reduce

input=sys.stdin.readline
p1, p2 = 97,1031
def comb(n,m,p):
    if n<m: 
        return 0
    return math.comb(n,m)%p

def f(n,m,p):
    if m==0: return 1
    if n==0: return 0
    aa = comb(n%p,m%p,p)
    bb= f(n//p,m//p,p)
    if aa==0: return 0
    return aa*bb%p
def powop(a, p, mo):
    rst=1
    while p:
        if p&1:
            rst*=a
            rst%=mo
        a*=a
        a%=mo
        p>>=1
    return rst

def crt(r1, m1, r2, m2):
    a1=powop(m2%m1, m1-2, m1)
    a2=powop(m1%m2, m2-2, m2)
    return (r1*m2*a1+r2*m1*a2)%(m1*m2)

def ff():
    a,b=map(int,input().split())
    if a==0 and b==1:
        print(1)
        return
    if a==0 and b!=1:
        print(0)
        return  
    a1 =f(a-1,b-2,p1)
    b1= f(a-1,b-2,p2)
    print(crt(a1,p1,b1,p2))
for _ in range(int(input())):
    ff()