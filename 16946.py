import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(N)]
re=[[0]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "1":
            arr[i][j] = -1
        else:
            arr[i][j] = 0

kk=1
ch=[[0]*M for _ in range(N)]

def bfs(a,b):
    global kk
    que=deque([(a,b)])
    c=0
    tmp=deque([])
    while que:
        c+=1
        x, y = que.popleft()
        tmp.append((x,y))
        arr[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    que.append((nx, ny))
    while tmp:
        x,y=tmp.popleft()
        arr[x][y] = c
        ch[x][y]=kk
        


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            kk+=1
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            t=0
            ttmp=[]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] != -1:
                        ttmp.append((arr[nx][ny],ch[nx][ny]))
            settmp=set(ttmp)
            for a,b in settmp:
                t+=a%10
            re[i][j] =t+1

# print(*arr,sep='\n')
# print(*re,sep='\n')
# print(*ch,sep='\n')
for i in range(N):
    for j in range(M):
        print(re[i][j]%10, end='')
    print()