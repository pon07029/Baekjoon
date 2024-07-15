import sys
input = sys.stdin.readline
n = int(input())
g=[]
eat=0
size=2
dd=0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
for i in range(n):
    g.append(list(map(int, input().split())))

def bfs():
    global eat, size
    dis=0
    li = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] == 9:
                que=[(i,j)]
                g[i][j] = 0
                li[i][j] = 1
                # print("시작하는 지점", i+1, j+1, size, dd)
    while que:
        tmp=[]
        dis+=1
        pp=[]
        for x, y in que:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if li[nx][ny] == 0 and g[nx][ny] <= size:
                        li[nx][ny] = 1
                        pp.append((nx,ny))
        pp.sort(key=lambda x:(x[1]))
        pp.sort(key=lambda x:(x[0]))
        # print(pp)
        for nx, ny in pp:
            # print("현재 위치", nx+1, ny+1, g[nx][ny],size )
            if  g[nx][ny] != 0 and g[nx][ny] < size:
                eat+=1
                if eat == size:
                    size+=1
                    eat=0
                g[nx][ny] = 9
                que=[]
                return dis
            tmp.append((nx, ny))
        que=tmp
    return 0

while True:
    a = bfs()
    dd+=a
    if a == 0:
        break
        
print(dd)
        



