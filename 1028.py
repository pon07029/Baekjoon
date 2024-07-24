import sys
N, M = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
dp = {}
def f(now, vi):
    if vi == (1 << N) - 1:
        if li[now][0]:
            return li[now][0]
        else:
            return int(1e9)
    if (now, vi) in dp:
        return dp[(now, vi)] 
    mi = int(1e9)
    for next in range(1, N):
        if li[now][next] == 0 or vi & (1 << next):
            continue
        cost = f(next, vi | (1 << next)) + li[now][next]
        mi = min(cost, mi)

    dp[(now, vi)] = mi 
    return mi  
print(f(0, 1))  

def ff(c):
    t=0
    for i in range(N):
        if c & (1 << i):
            t+=1
    return t