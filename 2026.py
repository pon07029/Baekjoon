import sys
input=sys.stdin.readline
K, N, F= map(int, input().split())
g={}
for i in range(N):
    g[i+1]=set({})
for _ in range(F):
    a, b =map(int, input().split())
    g[a].add(b)
    g[b].add(a)

def f(arr):
    if len(arr)==K:
        print(*arr, sep="\n")
        exit()
    for i in range(arr[-1]+1, N+1):
        for j in arr:
            if j not in g[i]:
                break
        else:
            f(arr+[i])
for i in range(1, N+1):
    f([i])
print(-1)

