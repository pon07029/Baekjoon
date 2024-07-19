import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M= map(int, input().split())
li=[list(input()) for _ in range(N)]
re=[[False]*M for _ in range(N)]
c=0

def f(w,i,j):
    if w=="D":
        return i+1,j
    elif w=="U":
        return i-1,j
    elif w=="R":
        return i,j+1
    elif w=="L":
        return i,j-1
    
def ff(a,b, arr):
    global c
    if re[a][b]:
        if (a,b) in arr:
            c+=1
        return
    else:
        re[a][b]=True
        w=li[a][b]
        i,j=f(w,a,b)
        ff(i,j,arr+[(a,b)])

for i in range(N):
    for j in range(M):
        if not re[i][j]:
            ff(i,j,[])

print(c)