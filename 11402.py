import math
def comb(n,m,p):
    if n<m: 
        print(0)
        exit()
    return math.comb(n,m)%p

def f(n,m,p):
    if n==0 or m==0: return 1
    return comb(n%p,m%p,p)*f(n//p,m//p,p)%p
a,b,c=map(int,input().split())
print(f(a,b,c))