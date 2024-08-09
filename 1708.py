import sys
from functools import cmp_to_key

N=int(sys.stdin.readline().rstrip())

points=[]
for i in range(N):
    points.append(list(map(int,sys.stdin.readline().rstrip().split())))

points=sorted(points,key=lambda x:(x[1],x[0]))
base=points[0][:]
del points[0]

def cmpccw(a,b): #벡터 base-a, base-b의 외적, ccw:1 cw:-1 0이면 a가 짧으면:1, 길면: -1 반환
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

print(len(ans))
