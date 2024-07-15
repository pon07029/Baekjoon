import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
g = {n:[] for n in range(1,N+1)}
li=[0]*(N+1)
mx=0
for i in range(N):
    dat = list(map(int, input().split()))
    a = dat[0]
    for j in range(1,len(dat)-2,2):
        b,c = dat[j],dat[j+1],
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