import sys
import heapq  
n, M=  map(int, sys.stdin.readline().split())
g={}
start = str(input())
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


def dijkstra():
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
    
for _ , p in dijkstra().items():
    print(p if p != float('inf') else "INF")