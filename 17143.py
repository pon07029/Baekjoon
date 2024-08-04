import sys
input=sys.stdin.readline
R, C, M = map(int, input().split())
arr=[[[] for j in range(M)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1]=(s,d,z)
# print(*arr, sep='\n')
ja=[]

def eat(n):
    for i in range(R):
        if arr[i][n]:
            ja.append(arr[i][n][2])
            arr[i][n].pop()
            return

def move():
    tmp=[[[] for j in range(M)] for _ in range(R)]
    for i in range(R):
        for j in range(M):
            if arr[i][j]:
                s, d, z = arr[i][j]
                if d==1 or d==2:
                    s%=2*(R-1)
                    if d==1:
                        if i-s<0:
                            s=i-s
                            d=2
                    else:
                        if i+s>=R:
                            s=2*(R-1)-s
                            d=1
                    tmp[i+s][j]=(s,d,z)
                else:
                    s%=2*(C-1)
                    if d==3:
                        if j+s>=C:
                            s=2*(C-1)-s
                            d=4
                    else:
                        if j-s<0:
                            s=j-s
                            d=3
                    tmp[i][j+s]=(s,d,z)
    arr=tmp

for i in range(C):
    eat(i)
    move()

print(sum(ja))