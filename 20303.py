import sys
from collections import deque
input=sys.stdin.readline
N, M, K = map(int,input().split())
g={}
vi=[False]*(N+1)
li=list(map(int,input().split()))
for i in range(M):
    a,b=map(int,input().split())
    if a in g:
        g[a].append(b)
    else:
        g[a]=[b]
    if b in g:
        g[b].append(a)
    else:
        g[b]=[a]
re=[]
for i in range(1,N+1):
    if not vi[i]:
        q=deque([i])
        vi[i]=True
        cnt=0
        su=0
        while q:
            x=q.popleft()
            cnt+=1
            su+=li[x-1]
            if x in g:
                for i in g[x]:
                    if not vi[i]:
                        vi[i]=True
                        q.append(i)
        re.append((cnt,su))

dp=[0]*(K)
for w, v in re:
    for i in range(K-1,w-1,-1):
        dp[i]=max(dp[i],dp[i-w]+v)
print(dp[K-1])