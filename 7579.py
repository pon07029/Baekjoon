n, k = map(int, input().split())

M=[0]+list(map(int, input().split()))
C=[0]+list(map(int, input().split()))
dp = [[0 for o in range(sum(C)+1) ]for _ in range(n+1)]
re=sum(C)
for i in range(1, n+1):
    weight = C[i]
    value = M[i]
    for j in range(1, sum(C)+1):
        
        if j < weight:  
            dp[i][j] = dp[i - 1][j]  
        else: 
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        if dp[i][j] >=k:
            re=min(re, j)
if sum([M[i] for i in range(1, n+1) if C[i]==0])>=k:
    print(0)
    exit()
if k!=0:
    print(re)
else:
    print(0)


