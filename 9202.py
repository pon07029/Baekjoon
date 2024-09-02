import sys
input=sys.stdin.readline
w=int(input())
words=[input().strip() for _ in range(w)]
g={}
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]
for i in range(w):
    fr=words[i][0]
    if fr in g:
        g[fr].append(i)
    else:
        g[fr]=[i]
_=input()

def score(l): 
    if l==1 or l==2:
        return 0
    elif l==3 or l==4:
        return 1
    elif l==5:
        return 2
    elif l==6:
        return 3
    elif l==7:
        return 5
    else:
        return 11

def f():
    arr=[]
    sv=set()
    for _ in range(4):
        arr.append(list(input().strip()))
    def dfs(wnum, wl, l, fi, x,y):
        # print(words[wnum], wl, l, fi, x,y)
        if l==wl:
            return True
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=4 or ny<0 or ny>=4:
                continue
            if arr[nx][ny]==words[wnum][l] and (nx,ny) not in fi and dfs(wnum, wl, l+1, fi+[(nx,ny)], nx,ny):
                return True
        return False
    
    for i in range(4):
        for j in range(4):
            if arr[i][j] in g:
                for wnum in g[arr[i][j]]:
                    if words[wnum] not in sv:
                        if dfs(wnum, len(words[wnum]), 1, [(i,j)], i,j):
                            # print(words[wnum], len(words[wnum]))
                            sv.add(words[wnum])
    sc=0
    mx=0
    mxw=""
    for word in sorted((list(sv))):
        sc+=score(len(word))
        if len(word)>mx:
            mx=len(word)
            mxw=word                     
    print(sc, mxw, len(sv))
for _ in range(int(input())):
    f()
    _=input()