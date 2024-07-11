import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

count=0
def bfs(k):
    que =k
    while que:
        tmp=[]
        for i in que:
          x, y = i[0], i[1]
          
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < N and 0 <= ny < M:
              
                  if graph[nx][ny] == 0:
                      graph[nx][ny] = -1
                      tmp.append([nx, ny]) 
        que = tmp
bfs([[0,0]])

def cz():
    tp=[]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                ct=0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == -1:
                            ct+=1
                if ct > 1:
                    tp.append([i,j])
    return tp

while True:

    tmp =[]

    for i, j in cz():
        graph[i][j] = -1
        tmp.append([i,j])
    if not tmp:
        break
    bfs(tmp)
    count+=1

# print(*graph, sep="\n")
print(count)

