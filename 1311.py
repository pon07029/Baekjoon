import sys
sys.setrecursionlimit(30)
N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
dp=[0]*(2**N)
def f(now, vi):
    if now==N :
        return 0
    # print(now, vi)
    if dp[vi]:
        return dp[vi] 
    mi = int(1e7)
    for next in range(N):
        if vi & (1 << next):
            continue
        cost = f(now+1, vi | (1 << next)) + li[now][next]
        mi = min(cost, mi)

    dp[vi] = mi 
    return mi
print(min(f(1, 1 << i)+li[0][i] for i in range(N)))

