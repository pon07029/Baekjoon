import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
T=int(input())
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for _ in range(T):
    N,M=map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    vi=[[0]*M for _ in range(N)]
    g={}
    score=0

    key=input()
    tmp=[]
    for i in range(N):
        for j in range(M):
            if 65<=ord(arr[i][j])<=90:
                if arr[i][j] in g:
                    g[arr[i][j]].append((i,j))
                else:
                    g[arr[i][j]]=[(i,j)]
    for k in key:
        if k.upper() in g:
            for x,y in g[k.upper()]:
                arr[x][y]='.'
    start=[]
    for i in range(N):
        if arr[i][0]=='.':
            start.append((i,0))
        if arr[i][M-1]=='.':
            start.append((i,M-1))
        if arr[i][0]=='$':
            score+=1
            arr[i][0]='.'
            start.append((i,0))
        if arr[i][M-1]=='$':
            score+=1
            arr[i][M-1]='.'
            start.append((i,M-1))
        if 97<=ord(arr[i][0])<=123:
            tmp.append(arr[i][0])
            arr[i][0]="."
        if 97<=ord(arr[i][M-1])<=123:
            tmp.append(arr[i][M-1])
            arr[i][M-1]="."

    for j in range(M):
        if arr[0][j]=='.':
            start.append((0,j))
        if arr[N-1][j]=='.':
            start.append((N-1,j))
        if arr[0][j]=='$':
            score+=1
            arr[0][j]='.'
            start.append((0,j))
        if arr[N-1][j]=='$':
            score+=1
            arr[N-1][j]='.'
            start.append((N-1,j))
        if 97<=ord(arr[0][j])<=123:
            tmp.append(arr[0][j])
            arr[0][j]="."
        if 97<=ord(arr[N-1][j])<=123:
            tmp.append(arr[N-1][j])
            arr[N-1][j]="."
    for k in tmp:
        if k.upper() in g:
            for x,y in g[k.upper()]:
                arr[x][y]='.'
    for i in range(N):
        if arr[i][0]=='.':
            start.append((i,0))
        if arr[i][M-1]=='.':
            start.append((i,M-1))
        if arr[i][0]=='$':
            score+=1
            arr[i][0]='.'
            start.append((i,0))
        if arr[i][M-1]=='$':
            score+=1
            arr[i][0]='.'
            start.append((i,M-1))
        if 97<=ord(arr[i][0])<=123:
            tmp.append(arr[i][0])
            arr[i][0]="."
        if 97<=ord(arr[i][M-1])<=123:
            tmp.append(arr[i][M-1])
            arr[i][M-1]="."

    for j in range(M):
        if arr[0][j]=='.':
            start.append((0,j))
        if arr[N-1][j]=='.':
            start.append((N-1,j))
        if arr[0][j]=='$':
            score+=1
            arr[0][j]='.'
            start.append((0,j))
        if arr[N-1][j]=='$':
            score+=1
            arr[N-1][j]='.'
            start.append((N-1,j))
        if 97<=ord(arr[0][j])<=123:
            tmp.append(arr[0][j])
            arr[0][j]="."
        if 97<=ord(arr[N-1][j])<=123:
            tmp.append(arr[N-1][j])
            arr[N-1][j]="."
    save=[]
    def f(x,y):
        global score
        # print(x,y, "go")
        if x<0 or x>=N or y<0 or y>=M or arr[x][y]=='*' or vi[x][y] or 65<=ord(arr[x][y])<=90:
            return 0
        # print(x,y, "done")
        # print(ord(arr[x][y]))
        if arr[x][y]=="$":
            score+=1
            arr[x][y]='.'
        if 97<=ord(arr[x][y])<=123:
            k=arr[x][y]
            k=k.upper()
            # print(k,"k")
            arr[x][y]='.'
            if k in g:
                for c,d in g[k]:
                    arr[c][d]='.'
                    save.append((c,d))
                # g.pop(k)
        vi[x][y]=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            # print(i,nx,ny,"i")
            f(nx,ny)
    # print(start, "start")
    # print(score, "before")
    while start:
        for x,y in start:
            f(x,y)
        # print(save, "save")
        start=[]
        if save:
                for x,y in save:
                    for i in range(4):
                        nx,ny=x+dx[i],y+dy[i]
                        if nx<0 or nx>=N or ny<0 or ny>=M:
                            start.append((x,y))
                            vi[x][y]=0
                            break
                        if 0<=nx<N and 0<=ny<M and arr[nx][ny]=='.' and vi[nx][ny]:
                            vi[x][y]=0
                            start.append((x,y))
                            break
        save=[]
        # print(start, "start")
    # print(*arr, sep='\n')
    print(score)