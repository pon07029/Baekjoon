import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(sys.stdin.readline()) for _ in range(N)]
day = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque()
kkk=0
check =[[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            que.append((i, j))
            check[i][j] = True
        if graph[i][j] == "X":
            check[i][j] = True



def bfs():
    kk=0
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if check[nx][ny] == False:
                    check[nx][ny] = True
                    que.append((nx, ny))
                    if graph[nx][ny] == "P":
                    
                        kk+=1
    print(kk if kk !=0 else "TT")
                 
bfs()

