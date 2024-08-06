import math
from random import randrange
pli = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
n=int(input())
def power(x,y,p):
    if y<2: return (x**y)%p
    else:
        d = y//2
        if y%2 == 0: return (power(x,d,p)**2)%p 
        else: return (x*(power(x,d,p))**2)%p
        
def mr(n,a):
    s,d = 0,n-1
    while d%2 == 0: s += 1; d //= 2
    x = power(a,d,n)
    if x == 1 or x+1 == n: return True
    for i in range(0, s-1):
        x = power(x,2,n)
        if x+1 == n: return True
    return False
 
def isp(n):
    if n in pli: return True
    if n == 1 or n%2 == 0: return False
    for p in pli:
        if not mr(n,p): return False
    return True
    
def rho(n):
    if isp(n): return n
    if n == 1: return 1
    if n%2 == 0: return 2
    x,c,d = randrange(2,n),randrange(1,n),1
    y = x
    while d == 1:
        x = ((x**2%n)+c)%n
        y = ((y**2%n)+c)%n
        y = ((y**2%n)+c)%n
        d = math.gcd(n,abs(x-y))
        if d == n: return rho(n)
    if isp(d): return d
    else: return rho(d)

if isp(n): print(n-1)
else:
    g={}
    re=1
    while n != 1:
        t=rho(n)
        if t in g:
            g[t]+=1
        else:
            g[t]=1
        n//=t
    for k, v in g.items():
        re *= (k ** v //k*(k-1))
    print(re)
    

