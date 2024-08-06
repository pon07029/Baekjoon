import sys
import math
input=sys.stdin.readline
N=int(input())
n=1000000
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

def f(x):
    g={}
    while x>1:
        k=1
        for j in primes:
            if x%j==0:
                if j in g:
                    g[j]+=1
                else:
                    g[j]=1
                x//=j
                k=0
                break
        if k:
            if x in g:
                g[x]+=1
            else:
                g[x]=1
            break
    return g
for i in range(N):
    a,b=map(int,input().split())
    insu=f(b)
    mi=[]
    for k,v in insu.items():
        p=1
        su=0
        no=k
        while True:
            if no>a:
                break
            su+=a//no
            no*=k
        mi.append(su//v)
    print(min(mi))
