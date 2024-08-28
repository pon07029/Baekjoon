
import sys
from functools import cmp_to_key
import math

# 점과 직선 사이의 거리
def cal_dist(x1, y1, x2, y2, a, b):
    area = abs((x1-a) * (y2-b) - (y1-b) * (x2 - a))
    AB = ((x1-x2)**2 + (y1-y2)**2) **0.5
    distance = area/AB
    return distance

def cmpccw(a,b): #벡터 base-a, base-b의 외적, ccw:1 cw:-1 0이면 a가 짧으면:1, 길면: -1 반환
    global base
    v1=[a[0]-base[0],a[1]-base[1]]
    v2=[b[0]-base[0],b[1]-base[1]]
    if (v1[0]*v2[1])-(v1[1]*v2[0])>0:
        return 1
    elif (v1[0]*v2[1])-(v1[1]*v2[0])<0:
        return -1
    else:
        if (v1[0]**2+v1[1]**2)>(v2[0]**2+v2[1]**2):
            return -1
        else:
            return 1

def ccw(a,b,c,d): #벡터 a-b, c-d의 외적 ccw:1 cw:-1 line:0
    v1=[b[0]-a[0],b[1]-a[1]]
    v2=[d[0]-c[0],d[1]-c[1]]
    if (v1[0]*v2[1])-(v1[1]*v2[0])>0:
        return 1
    elif (v1[0]*v2[1])-(v1[1]*v2[0])<0:
        return -1
    else:
        return 0

def f():
    global base
    N=int(sys.stdin.readline().rstrip())
    if N==0:
        exit()
    points=[]
    for i in range(N):
        points.append(list(map(int,sys.stdin.readline().rstrip().split())))

    points=sorted(points,key=lambda x:(x[1],x[0]))
    base=points[0][:]
    del points[0]


    points=sorted(points,key=cmp_to_key(cmpccw),reverse=True)

    ans=[]
    ans.append(base)
    ans.append(points[0])
    for i in range(1,N-1):
        new=points[i]
        if ccw(ans[-2],ans[-1],ans[-1],new)==1:
            ans.append(new)
            
        elif ccw(ans[-2],ans[-1],ans[-1],new)==-1:
            ans.pop()
            while ccw(ans[-2],ans[-1],ans[-1],new)<=0:
                ans.pop()
            ans.append(new)
            
        elif ccw(ans[-2],ans[-1],ans[-1],new)==0:
            ans.pop()
            ans.append(new)
    mi=99999999999

    ans=ans+[ans[0]]
    # print(ans)
    l=len(ans)
    for i in range(l-1):
        x1,y1=ans[i]
        x2,y2=ans[i+1]
        mx=0
        for j in range(l):
            if i==j or j==i+1:
                continue
            # print(j)
            a,b=ans[j]
            dis = cal_dist(x1,y1,x2,y2,a,b)
            # print(x1,y1,x2,y2,a,b,dis)
            if dis:
                mx=max(mx,dis)
        mi=min(mi,mx)
    global num
    mi= math.ceil(mi * 100) / 100
    print(f"Case {num}: %.2f"%mi)
    num+=1
num=1
while True:
    # num=1
    f()