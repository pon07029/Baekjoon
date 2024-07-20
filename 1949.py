import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li=[list(map(int, input().split())) for _ in range(N)]
re=[[-1]*M for _ in range(N)]
re[0][0]= li[0][0]
for i in range(1, M):
    re[0][i]=re[0][i-1]+li[0][i]

def f(n,m,b):
    if re[n][m]:
        return re[n][m]
    tmp=[f(n-1,m,0)]
    if m>0 and b!=1:
        tmp.append(f(n,m-1,-1))
    if m<M-1 and b!=-1:
        tmp.append(f(n,m+1,+1))
    re[n][m] = max(tmp)
    return re[n][m]

print(f(5,5,0))

