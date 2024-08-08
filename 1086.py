import sys
N = int(input())
li = []
for i in range(N):
    li.append(int(input()))
K = int(input())
dp = {}
tm=[0]*K
def f(now, vi):
    newvi= vi | (1 << now)
    if newvi in dp:
        return 
    tmp=[0]*K
    tp=dp[vi]
    for i in range(K):
        # print(li[now], i, vi)
        # print((tp[i]*(10**(len(str(li[now]))))+li[now]))
        na=(tp[i]*(10**(len(str(li[now]))))+li[now])%K
        # print(na)
        tmp[na]+=tp[i]+1
    dp[newvi]=tmp
    for next in range(1, N):
        if newvi & (1 << next):
            continue
        f(next, newvi)
    return 
dp[0]=tm
for i in range(N):
    f(i, 0)
# print(sum(dp[(1 << N) - 1]) - 1)
print(dp[(1 << N) - 1])