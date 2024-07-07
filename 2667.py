#bfs 
N = int(input())
graph = [list(input()) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
re=[]
def bfs(start):
    que = [[start[0],start[1]]]
    count = 1
    while que:
        tmp=[]
        for i in que:
          x, y = i[0], i[1]
          graph[x][y] = "0"
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < N and 0 <= ny < N:
              
                  if graph[nx][ny] == "1":
                      count+=1
                      graph[nx][ny] = "0"
                      tmp.append([nx, ny])        
        que = tmp
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            re.append(bfs([i,j]))

re.sort()
print(len(re))
print(*re, sep='\n')