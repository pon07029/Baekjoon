import sys
from collections import deque
input=sys.stdin.readline
N, M = map(int,input().split())
li=[0 for _ in range(N+1)]
g=[[]for _ in range(N+1)]   
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    li[b]+=1
q=deque([])
for i in range(1,N+1):
    if li[i]==0:
        q.append(i)

re=[]
while q:
    x=q.popleft()
    re.append(x)
    for i in g[x]:
        li[i]-=1
        if li[i]==0:
            q.append(i)

print(*re)