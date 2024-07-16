import sys
input = sys.stdin.readline
N, M, L = map(int, input().split())
li=[]
for i in range(N):
    li.append(list(input())[:-1])
w=input()
tm=[]
re=[[0]*M for _ in range(N)]
dx=[1,1,1,0,0,-1,-1,-1]
dy=[1,0,-1,1,-1,1,0,-1]

def f(i,j,wo):
    tmp=[]
    for k in range(8):
        nx=i+dx[k]
        ny=j+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if li[nx][ny]==wo:
                tmp.append((nx,ny))
    return tmp

for i in range(N):
    for j in range(M):
        if li[i][j]==w[0]:
            re[i][j]=1
for p in range(1, L):
    tp=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if re[i][j]>0:
                t=re[i][j]
                for i1, j1 in f(i,j,w[p]):
                    
                    tp[i1][j1]+=t
    re=tp
print(sum(map(sum, re)))


