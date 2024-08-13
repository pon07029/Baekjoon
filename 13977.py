import sys
input = sys.stdin.readline
m=1000000007
li=[0]*4000001
li[0]=1
for i in range(1,4000001):
    li[i]=li[i-1]*i%m

def f(a, b):
    if a==0:
        return 1
    elif a%2==0:
        return (f(a//2, b)**2)%m
    else:
        return (f(a//2, b)**2*b)%m

M=int(input())
for i in range(M):
    N, K=map(int, input().split())
    print(li[N]*f(m-2, li[N-K])*f(m-2,li[K])%m)