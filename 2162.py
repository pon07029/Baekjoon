import sys
input=sys.stdin.readline

def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)
    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
    # 평행
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    # 교차
    else:
        if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
            return 1

    return 0

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

N=int(input())
li=[]
for _ in range(N):
    li.append(list(map(int,input().split())))

p=[i for i in range(N)]

def fp(x):
    if p[x]==x:
        return x
    p[x]=fp(p[x])
    return p[x]

def up(a,b):
    a=fp(a)
    b=fp(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b


for i in range(N):
    for j in range(N):
        if solution(li[i][0],li[i][1],li[i][2],li[i][3],li[j][0],li[j][1],li[j][2],li[j][3]):
            up(i,j)
            continue
for i in range(N):
    for j in range(N):
        if solution(li[i][0],li[i][1],li[i][2],li[i][3],li[j][0],li[j][1],li[j][2],li[j][3]):
            up(i,j)
            continue
li=set(p)
print(len(li))
mx=0
for i in li:
    if mx<p.count(i):
        mx=p.count(i)
print(mx)
