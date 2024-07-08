import sys
import heapq  
n ,N= map(int, sys.stdin.readline().split())
g={}
for i in range(N):
    a, b, c = map(str, sys.stdin.readline().split())
    if a in g:
        if b in g[a]:
            g[a][b] = min(g[a][b], int(c))
        else:
            g[a][b] = int(c)
    else:
        g[a] = {b:int(c)}
    if b in g:
        if a in g[b]:
            g[b][a] = min(g[b][a], int(c))
        else:
            g[b][a] = int(c)
    else:
        g[b] = {a:int(c)}
for i in range(1, n+1):
    if str(i) not in g:
        g[str(i)] = {}

## 그래프에 시작과 끝이 같고 비용이 다른 경우 여러번 들어가면 조심

A, B = map(str, sys.stdin.readline().split())



def dijkstra(start):
  dis = {str(i): float('inf') for i in range(1, n+1)}
  dis[start] = 0 
  q = []
  heapq.heappush(q, [dis[start], start])  

  while q:  
    nowdis, now = heapq.heappop(q) 

    if dis[now] < nowdis: 
      continue
    
    for newend, newdis in g[now].items():
      total = nowdis + newdis  
      if total < dis[newend]: 
        dis[newend] = total
        heapq.heappush(q, [total, newend]) 
    
  return dis
    
# print(dijkstra(A))
# print(dijkstra(B))
# print()
# print(dijkstra(str(n)))
k =min(dijkstra("1")[A] + dijkstra(A)[B] + dijkstra(B)[str(n)]
, dijkstra("1")[B] + dijkstra(A)[B] + dijkstra(A)[str(n)]
)
print(k if k < float('inf') else -1)