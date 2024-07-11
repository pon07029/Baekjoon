N, M = map(int, input().split())
import copy
graph = [list(map(int, input().split())) for _ in range(N)]
li=[]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

q=[]

def fun():
    g = copy.deepcopy(graph)
    que = q
    while que:
        tmp= []
        for i in que:
            x, y = i
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < N and 0 <= ny < M:
                    if g[nx][ny] == 0:
                        g[nx][ny] = 2
                        tmp.append([nx,ny])
        que=tmp
    c=0
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                c+=1

    return c

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            li.append([i,j])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            q.append([i,j])
mx=0
for i in range(len(li)):
    graph[li[i][0]][li[i][1]]=1
    for j in range(i+1,len(li)):
        graph[li[j][0]][li[j][1]]=1
        for k in range(j+1,len(li)):
            graph[li[k][0]][li[k][1]]=1
            # print(li[i],li[j],li[k], fun())
            mx=max(fun(),mx)
            graph[li[k][0]][li[k][1]]=0
        graph[li[j][0]][li[j][1]]=0
    graph[li[i][0]][li[i][1]]=0
print(mx)