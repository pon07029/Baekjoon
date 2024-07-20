W=list(input())
N=len(W)
dp=[[-1]*N for _ in range(N)]
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
print(*dp,sep="\n")
