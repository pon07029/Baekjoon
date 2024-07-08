import sys
N = int(sys.stdin.readline())
R=[]
G=[]
B=[]
for i in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    if i == 0:
        R.append(r)
        G.append(g)
        B.append(b)
    else:
        R.append(min(G[i-1], B[i-1])+r)
        G.append(min(R[i-1], B[i-1])+g)
        B.append(min(R[i-1], G[i-1])+b)
print(min(R[N-1], G[N-1], B[N-1]))