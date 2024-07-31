import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(N)]
re=[[0]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "1":
            arr[i][j] = -1
        else:
            arr[i][j] = 0




def bfs(a,b):
    que=deque([(a,b)])
    c=0
    tmp=[]
    while que:
        c+=1
        x, y = que.popleft()
        tmp.append((x,y))
        arr[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    que.append((nx, ny))
    for x,y in tmp:
        arr[x][y] = c


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            t=0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] != -1:
                        t+=arr[nx][ny]
            re[i][j] =t+1

print(*arr,sep='\n')
print(*re,sep='\n')