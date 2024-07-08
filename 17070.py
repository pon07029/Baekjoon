wall=[]
N=int(input())
for i in range(N):
    wall.append(list(map(int,input().split())))
li=[]
for i in range(N):
    li.append([[0,0,0] for j in range(N)])

def ch1(y,x):
    if x+1>=N:
        return 0
    if wall[y][x+1]==1:
        return 0
    return 1
def ch2(y,x):
    if x+1>=N:
        return 0
    if y+1>=N:
        return 0
    
    if wall[y][x+1] ==1 or wall[y+1][x] ==1 or wall[y+1][x+1] ==1:
        return 0
    return 1

def ch3(y,x):
    if y+1>=N:
        return 0
    if wall[y+1][x]==1:
        return 0
    return 1
li[0][1]=[1,0,0]

for j in range(N):
    for i in range(1,N):
        if li[j][i][0]:
            if ch1(j,i):
                li[j][i+1][0]+=li[j][i][0]
            if ch2(j,i):
                li[j+1][i+1][1]+=li[j][i][0]
        if li[j][i][1]:
            if ch1(j,i):
                li[j][i+1][0]+=li[j][i][1]
            if ch2(j,i):
                li[j+1][i+1][1]+=li[j][i][1]
            if ch3(j,i):
                li[j+1][i][2]+=li[j][i][1]
        if li[j][i][2]:
            if ch2(j,i):
                li[j+1][i+1][1]+=li[j][i][2]
            if ch3(j,i):
                li[j+1][i][2]+=li[j][i][2]
print(sum(li[N-1][N-1]))