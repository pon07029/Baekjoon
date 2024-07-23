import sys
sys.setrecursionlimit(10**6)
N, M =map(int, sys.stdin.readline().split())
arr=[list(sys.stdin.readline()) for _ in range(N)]
vi=[[0]*M for _ in range(N)]
li=[[-1]*M for _ in range(N)]

def f(x,y):
    if x<0 or y<0 or x>=N or y>=M:
        return 0
    if arr[x][y]=="H":
        return 0
    if vi[x][y]:
        print(-1)
        exit()
    if li[x][y]!=-1:
        return li[x][y]
    move= int(arr[x][y])
    # print(x,y,move, d)
    vi[x][y]=1
    li[x][y]=max(f(x+move, y), f(x-move, y),f(x, y-move), f(x, y+move))+1
    vi[x][y]=0
    return li[x][y]

print(f(0,0))
# print(*li, sep="\n")