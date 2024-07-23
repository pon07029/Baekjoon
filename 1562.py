N=int(input())
dp=[[[0]*10 for _ in range(1<<10)] for _ in range(N)]
for i in range(10):
    dp[0][1<<i][i]=1
for i in range(N-1): # n-1까지하면 n 구할수 있음
  for j in range(10):
    for b in range(1024):
      if 0<=j<9:
        tp = b | 1<<(j+1)
        dp[i+1][tp][j+1] += dp[i][b][j]
        dp[i+1][tp][j+1] %= 1000000000
      if 0<j<=9:
        tp = b | 1<<(j-1)
        dp[i+1][tp][j-1] += dp[i][b][j]
        dp[i+1][tp][j-1] %= 1000000000

t = 0
for k in range(1,10): # 0으로 시작하는 수만 제외
  t += dp[N-1][1023][k]
  t%=1000000000
print(t)
