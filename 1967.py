import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
g = {n:[] for n in range(1,N+1)}
li=[0]*(N+1)
mx=0
for i in range(N-1):
    a,b,c = map(int, input().split())
    g[a].append((b,c))
    g[b].append((a,c))

def f(st, dis):
   for no, di in g[st]:
        if vi[no] == -1:
            vi[no] = dis + di
            f(no, dis + di)

vi = [-1]* (N+1)
vi[1] = 0
f(1,0)
long = vi.index(max(vi))
vi = [-1]* (N+1)
vi[long] = 0
f(long,0)
print(max(vi))