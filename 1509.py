import sys
sys.setrecursionlimit(10**6)

W=list(input())
N=len(W)
dp=[[-1]*N for _ in range(N)]
li=[0]*(N+1)
for i in range(N):
    dp[i][i]=1
def pel(s,e):
    if s>=e:
        return 1
    if dp[s][e]!=-1:
        return dp[s][e]
    if W[s]==W[e]:
        dp[s][e]=pel(s+1,e-1)
    else:
        dp[s][e]=0
    return dp[s][e]
for i in range(N):
    for j in range(i):
        pel(j,i)
# print(*dp,sep="\n")

def f(k):
    if k>=N:
        return 0
    if li[k]:
        return li[k]
    li[k]=min([f(i+1)+1 for i in range(k,N) if dp[k][i]==1])
    return li[k]
    
print(f(0))
