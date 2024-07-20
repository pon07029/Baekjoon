import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Ns = list(map(int, input().split()))
Ms = list(map(int, input().split()))

if N<M:
    N,M = M,N
    Ns, Ms = Ms, Ns

Ns.sort()
Ms.sort()

li=[[0]*M for i in range(N)]
re=[[-1]*M for i in range(N)]
for i in range(N):
    for j in range(i,M):
        li[i][j]=abs(Ns[i]-Ms[j])

def f(a,b):
    if b ==0:
        return li[a][b]
    if re[a][b]!=-1:
        return re[a][b]
    re[a][b]=min([f(i-1,b-1) for i in range(b,a+1)])+li[a][b]
    return re[a][b]
# for k in range(M,N+1):
#     print(k,M-1, f(k-1,M-1))

print(min(f(k-1,M-1) for k in range(M,N+1)))