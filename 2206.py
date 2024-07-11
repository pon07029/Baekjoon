#bfs 
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
day = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

mo = [[0]*M for _ in range(N)]
mu = [[0]*M for _ in range(N)]
def bfs():
    que = [[0,0]]
    mo[0][0]=1
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
              
                  if graph[nx][ny] == "0" and mo[nx][ny] == 0:
                      mo[nx][ny] = move
                      tmp.append([nx, ny])
          
        que = tmp

def bfs2():
    que = [[N-1,M-1]]
    mu[N-1][M-1]=1
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
              
                  if graph[nx][ny] == "0" and mu[nx][ny] == 0:
                      mu[nx][ny] = move
                      tmp.append([nx, ny])
          
        que = tmp


max=999999999
bfs()
if mo[N-1][M-1] >0:
    max=mo[N-1][M-1]

bfs2()

for i in range(N):
    for j in range(M):
        if graph[i][j] == "1":
            for k in range(4):
              nx = i + dx[k]
              ny = j + dy[k]
              if 0 <= nx < N and 0 <= ny < M:
                  if mo[nx][ny] > 0:
                    for l in range(4):
                        nnx = i + dx[l]
                        nny = j + dy[l]
                        if 0 <= nnx < N and 0 <= nny < M:
                            if mu[nnx][nny] > 0:
                    
                                max = min(max,  mo[nx][ny]+mu[nnx][nny]+1)

# print(*mo, sep = "\n")
# print(*mu, sep = "\n")
print(max if max != 999999999 else -1)