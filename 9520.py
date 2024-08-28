import sys
input = sys.stdin.readline
N, M, Q= map(int, input().split())
ap=list(map(int, input().split()))
yo=list(map(int, input().split()))
N=len(ap)
dp=[1999999999]*(N+1)
dp[M]=ap[M-1]-ap[0]
sv=[0]*N
sv[M-1]=ap[0]
for i in range(M+1, N+1):
    a =max(dp[i-1],ap[i-1]-sv[i-2])
    b= max(ap[i-1]-ap[i-M], dp[i-M])
    if a>=b:
        sv[i-1]=ap[i-M]
        dp[i]=b
    else:
        sv[i-1]=sv[i-2]
        dp[i]=a
cha=dp[-1]
print(dp)
print(sv)
for i in yo:
    if i>=cha:
        print("1", end="")
    else:  
        print("0", end="")