R=[]
G=[]
B=[]
re=[]
N = int(input())
for i in range(N):
    r,g,b=map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

Rs=[[9999999,9999999,9999999] for _ in range(N)]
Rs[0][0]=R[0]
for i in range(1,N):
    Rs[i][0]=min(Rs[i-1][1], Rs[i-1][2])+R[i]
    Rs[i][1]=min(Rs[i-1][0], Rs[i-1][2])+G[i]
    Rs[i][2]=min(Rs[i-1][0], Rs[i-1][1])+B[i]

Gs=[[9999999,9999999,9999999] for _ in range(N)]
Gs[0][1]=G[0]
for i in range(1,N):
    Gs[i][0]=min(Gs[i-1][1], Gs[i-1][2])+R[i]
    Gs[i][1]=min(Gs[i-1][0], Gs[i-1][2])+G[i]
    Gs[i][2]=min(Gs[i-1][0], Gs[i-1][1])+B[i]

Bs=[[9999999,9999999,9999999] for _ in range(N)]
Bs[0][2]=B[0]
for i in range(1,N):
    Bs[i][0]=min(Bs[i-1][1], Bs[i-1][2])+R[i]
    Bs[i][1]=min(Bs[i-1][0], Bs[i-1][2])+G[i]
    Bs[i][2]=min(Bs[i-1][0], Bs[i-1][1])+B[i]


print(min(Rs[-1][1], Rs[-1][2], Gs[-1][0], Gs[-1][2], Bs[-1][0], Bs[-1][1]))