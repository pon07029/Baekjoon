import math
N, R, G, B =map(int, input().split())
li = [[[-1 for k in range(B+1)]for j in range(G+1)] for i in range(R+1)]

def f(h,r,g,b):
    if h>N:
        return 1
    if li[r][g][b]!=-1:
        return li[r][g][b]
    tmp=0
    if r>=h:
        tmp += f(h+1,r-h,g,b)
    if g>=h:
        tmp += f(h+1,r,g-h,b)
    if b>=h:
        tmp += f(h+1,r,g,b-h)
    
    if h%2==0:
        p=h//2
        c= math.comb(h,p)
        if r>=p and g>=p:
            tmp += f(h+1,r-p,g-p,b)*c
        if r>=p and b>=p:
            tmp += f(h+1,r-p,g,b-p)*c
        if g>=p and b>=p:
            tmp += f(h+1,r,g-p,b-p)*c
    if h%3==0:
        p=h//3
        c= math.comb(h,p)*math.comb(h-p,p)
        if r>=p and g>=p and b>=p:
            tmp += f(h+1,r-p,g-p,b-p)*c
    li[r][g][b]=tmp
    return tmp

print(f(1,R,G,B))