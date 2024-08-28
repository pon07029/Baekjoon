import sys
from collections import deque  
input= sys.stdin.readline
n= int(input())
M= int(input())
g=[[]for i in range(n+1)]
gb=[[]for i in range(n+1)]
deg=[0]*(n+1)
dis=[0]*(n+1)
for i in range(M):
    a, b, c = map(int, input().split())
    g[a].append([b,c])
    gb[b].append([a,c])
    deg[b]+=1
st,ed= map(int, input().split())

q=deque()
q.append(st)
while q:
    now = q.popleft()
    for i in g[now]:
        deg[i[0]]-=1
        dis[i[0]]=max(dis[i[0]],dis[now]+i[1])
        if deg[i[0]]==0:
            q.append(i[0])
longest=dis[ed]
q=deque()
q.append(ed)
ch=[False]*(n+1)
cnt=0
while q:
    now = q.popleft()
    for i in gb[now]:
        if dis[i[0]]+i[1]==dis[now]:
            cnt+=1
            if not ch[i[0]]:
                ch[i[0]]=True
                q.append(i[0])
print(longest)
print(cnt)