import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [list(input()) for _ in range(N)]
graph2 =[["A"]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph2[i][j] = 'G'
        else:
            graph2[i][j] = graph[i][j]



dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque()


def bfs(now):
    now=now
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == now:
                    graph[nx][ny] = "C"
                    que.append((nx, ny))
def bfs2(now):
    now=now
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph2[nx][ny] == now:
                    graph2[nx][ny] = "C"
                    que.append((nx, ny))
g1=0
for i in range(N):
    for j in range(N):
        if graph[i][j] !="C":
            que.append((i, j))
            bfs(graph[i][j])
            g1+=1
g2=0
for i in range(N):
    for j in range(N):
        if graph2[i][j] !="C":
            que.append((i, j))
            bfs2(graph2[i][j])
            g2+=1

print(g1, g2)