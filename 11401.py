m=1000000007

def fa(n):
    if n==0:
        return 1
    for i in range(1,n):
        n*=i
        n%=m
    return n

def f(a, b):
    if a==0:
        return 1
    elif a%2==0:
        return (f(a//2, b)**2)%m
    else:
        return (f(a//2, b)**2*b)%m

N, K=map(int, input().split())
print(fa(N)*f(m-2, fa(N-K))*f(m-2, fa(K))%m)