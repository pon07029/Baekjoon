import sys
sys.setrecursionlimit(10**6)
N = int(input())
li = []
for _ in range(N):
    l=list(input())
    li.append([int(i) for i in l])
dp = {}
best=0
def ff(c):
    global best
    t=0
    for i in range(N):
        if c & (1 << i):
            t+=1
    best=max(best,t)
def f(now, vi,nc):
    ff(vi)
    if vi == (1 << N) - 1:
        print(N)
        exit()
    if (now, vi) in dp:
        if dp[(now, vi)]>nc:
            dp[(now, vi)] = nc
        else:
            return
    for next in range(0, N):
        if li[now][next] <nc or vi & (1 << next):
            continue
        f(next, vi | (1 << next),li[now][next])

    dp[(now, vi)] = nc
    return 

f(0, 1,0)
# print(dp)
print(best)