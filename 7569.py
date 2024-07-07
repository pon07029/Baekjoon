import sys
from collections import deque
input = sys.stdin.readline
M, N, O = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(O)]
day = 0
dx = [1,0,-1,0 ,0 ,0]
dy = [0,1,0,-1, 0, 0]
dz = [0, 0 ,0 ,0 ,1, -1]
que = deque()
for i in range(N):
    for j in range(M):
        for k in range(O):
            if graph[k][i][j] == 1:
                que.append((k ,i, j))

def bfs():
    while que:
        z, y, x = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < O:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    que.append((nz, ny, nx))

bfs()
for i in range(N):
    for j in range(M):
        for k in range(O):
          if graph[k][i][j] == 0:
              print(-1)
              sys.exit()
          day = max(day,graph[k][i][j])
print(day-1)