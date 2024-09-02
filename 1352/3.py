N=int(input())
dp=[(0,0)]*(N+1)
mod=1000000007
dp[1]=(2,1)
for i in range(2, N+1):
    dp[i]=(2*(dp[i-1][0]+dp[i-1][1])%mod, dp[i-1][0])
# print(*dp, sep='\n')
print((dp[N][0]+dp[N][1])%mod)