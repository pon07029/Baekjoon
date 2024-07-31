import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R ,Q = map(int, input().split())
vi = [False]*(N+1)
re = [0]*(N+1)
g={}
for i in range(N-1):
    a, b = map(int, input().split())
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]
    if b in g:
        g[b].append(a)
    else:
        g[b] = [a]
li=[]
for i in range(Q):
    li.append(int(input()))

def f(n):
    vi[n] = True
    re[n] = 1
    if n in g:
        for i in g[n]:
            if not vi[i]:
                re[n] += f(i)
    return re[n]
f(R)
for i in li:
    print(re[i])