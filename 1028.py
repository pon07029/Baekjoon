import sys
input=sys.stdin.readline
N, M =map(int, input().split())
li = []
for _ in range(N):
    li.append(list(input().rstrip()))
tmp=[]
for i in range(N):
    for j in range(M):
        if li[i][j]=="1":
            tmp.append((i,j))

def f(x,y,size):
    for i in range(size):
        if li[x+i+size-1][y-size+1+i]!="1" or li[x+i+size-1][y+size-1-i]!="1":
            return False
    return True
def ff(x,y,size):
    i=size-1
    if li[x+i][y-i]!="1" or li[x+i][y+i]!="1":
            return False
    return True

siz=1
mx=0
if tmp:
    mx=1
while tmp:
    # print(siz, tmp)
    siz+=1
    tm=[]
    for i, j in tmp:
        if j>=siz-1 and i<N-siz-siz+2 and j <= M-siz:
            if ff(i,j,siz):
                # print(i,j)
                tm.append((i,j))
                if f(i,j,siz):
                    mx=siz
    tmp=tm
print(mx)