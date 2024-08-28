import sys
import copy
input = sys.stdin.readline
li=[]
in_range = lambda y, x: 0 <= y < 10 and 0 <= x < 10
dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]


def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if in_range(ny, nx):
            b[ny][nx] = (b[ny][nx] + 1) % 2
mi=[]
for i in range(10):
    k=list(input().strip())
    tmp=[]
    for j in k:
        if j=="#":
            tmp.append(0)
        else:
            tmp.append(1)
    li.append(tmp)

for i in range(1<<10):
    nb = copy.deepcopy(li)
    # print(bin(i))
    cnt=0
    for j in range(10):
        
        if i & (1<<j):
            # print(bin(i), bin(1<<j))    
            press(nb, 0, j)
            cnt+=1

    for j in range(1,10):
        for k in range(10):
            if nb[j-1][k]:
                press(nb, j, k)
                cnt+=1
    if sum(nb[-1])==0:
        mi.append(cnt)
print(min(mi))