import sys
import heapq  
n, M, end = map(int, sys.stdin.readline().split()) 
g={}
for i in range(M):
    a, b, c = map(str, sys.stdin.readline().split())
    if a in g:
        if b in g[a]:
            g[a][b] = min(g[a][b], int(c))
        else:
            g[a][b] = int(c)
    else:
        g[a] = {b:int(c)}
for i in range(1, n+1):
    if str(i) not in g:
        g[str(i)] = {}


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
ret = dijkstra(str(end))
mxx=0
for i in range(1, n+1):
    mxx=max(dijkstra(str(i))[str(end)]+ret[str(i)],mxx)

print(mxx)