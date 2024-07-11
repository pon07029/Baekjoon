import sys
N, M = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
mx=0
vis=[False]*26
vis[ord(graph[0][0])-65]=True
def dfs_recursive(x,y,c):
    global mx

    for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                v=ord(graph[nx][ny])-65
                if vis[v] ==False:
                    vis[v] =True
                    dfs_recursive(nx, ny, c+1)
                    vis[v] =False
    mx=max(mx,c)


dfs_recursive(0,0,1)

print(mx)