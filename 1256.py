import math
N , M ,K = map(int, input().split())

def f(n,m,k):
    
    if n==0:
        return "z"*m
    if m==0:
        return "a"*n
    t=math.comb(n+m-1,n-1)
    # print(n,m,k, t)
    if k>=t:
        return "z"+f(n,m-1,k-t)
    else:
        return "a"+f(n-1,m,k)
if math.comb(N+M,N)<K:
    print(-1)  
    exit()  

print(f(N,M,K-1))