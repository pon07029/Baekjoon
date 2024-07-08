import sys
N, M = map(int, sys.stdin.readline().split())
li=[]
for i in range(N):
    dat = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N):
        dat[j] += dat[j-1]
    li.append(dat)
for i in range(1, N):
    for j in range(N):
        li[i][j] += li[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    result=0
    if x2 ==0:
        if y2 ==0:
            result = li[x2][y2] 
        else:
            result = li[x2][y2] - li[x2][y1-1]
    elif y2 ==0:
        result = li[x2][y2] - li[x1-1][y2]
    else:
        if x1 == 0:
            if y1 == 0:
                result = li[x2][y2]
            else:
                result = li[x2][y2] - li[x2][y1-1]
        elif y1 == 0:
            result = li[x2][y2] - li[x1-1][y2]
        else:
            result = li[x2][y2] - li[x1-1][y2] - li[x2][y1-1] + li[x1-1][y1-1]

    
    print(result)