import sys
input = sys.stdin.readline
N, M, T = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
up, down = 0, 0
for i in range(N):
        if li[i][0] == -1:
            up = i
            break
down = up + 1
def air():
    tmp = [[0]*M for _ in range(N)]
    tmp[up][0] = -1
    tmp[down][0] = -1
    for i in range(N):
        for j in range(M):
            if li[i][j] > 0:
                cnt = 0
                ai =li[i][j]//5
                for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < N and 0 <= ny < M and li[nx][ny] != -1:
                        tmp[nx][ny] += ai
                        cnt += 1
                tmp[i][j] += li[i][j] - ai*cnt
    for i in range(N):
        for j in range(M):
            li[i][j] = tmp[i][j]

def clean():
    for i in range(1, up):
        li[i][0] = li[i-1][0]
    for i in range(M-1):
        li[0][i] = li[0][i+1]
    for i in range(0,up):
        li[i][M-1] = li[i+1][M-1]
    for i in range(M-1, 1, -1):
        li[up][i] = li[up][i-1]
    li[up][1] = 0
    for i in range(down+1, N-1):
        li[i][0] = li[i+1][0]
    for i in range(M-1):
        li[N-1][i] = li[N-1][i+1]
    for i in range(N-1, down, -1):
        li[i][M-1] = li[i-1][M-1]
    for i in range(M-1, 1, -1):
        li[down][i] = li[down][i-1]
    li[down][1] = 0

for _ in range(T):
    air()
    clean()
    # print(*li, sep='\n')
    print(sum([sum(li[i]) for i in range(N)])+2)
print(sum([sum(li[i]) for i in range(N)])+2)