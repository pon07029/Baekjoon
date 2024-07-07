#bfs 
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
day = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

mo = [[0]*M for _ in range(N)]
mo[0][0]=1

def bfs():
    que = [[0,0]]
    move =1
    while que:
        
        tmp=[]
        move+=1
        for i in que:
          x, y = i[0], i[1]
          
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < N and 0 <= ny < M:
              
                  if graph[nx][ny] == "1" and mo[nx][ny] == 0:
                      mo[nx][ny] = move
                      tmp.append([nx, ny])
          
        que = tmp


bfs()
print(mo[N-1][M-1])