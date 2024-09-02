import sys
from collections import deque
input=sys.stdin.readline
N, K, D = map(int, input().split())
stu=[(0,0)]*(N)
al=[]
sa=[0]*(K+1)

for i in range(N):
    a, b = map(int, input().split())
    stu[i]=(i,b)
    al.append(list(map(int, input().split())))
stu.sort(key=lambda x:x[1])
mx=0
now=deque([])
for p, d in stu:
    #버리기
    #더하기
    #계산
    # print(now[0][1], d-D)
    while now and now[0][1]<d-D:
        np, nd =now.popleft()
        for j in al[np]:
            sa[j]-=1
    for j in al[p]:
        sa[j]+=1
    now.append((p,d))
    l=len(now)
    mx=max(mx, sum([l for i in sa if i>0 and i<l]))
    # print(sa)
    # print(now)
print(mx)