import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input())
g={}
dp=[[0,0] for i in range(N+1)]
vi=[False]*(N+1)
for i in range(N):
    g[i+1]=[]

for i in range(N-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def f(n):
    vi[n]=True
    for i in g[n]:
        if vi[i]:
            continue
        f(i)
        dp[n][0]+=dp[i][1]
        dp[n][1]+=min(dp[i][0],dp[i][1])
    dp[n][1]+=1
    return
f(1)
print(min(dp[1][0],dp[1][1]))