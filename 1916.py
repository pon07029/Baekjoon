import sys
import heapq  
n = int(sys.stdin.readline())
g={}
for i in range(int(sys.stdin.readline())):
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

## 그래프에 시작과 끝이 같고 비용이 다른 경우 여러번 들어가면 조심

start, end = map(str, sys.stdin.readline().split())

if start == end:
    print(0)
    sys.exit()

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
    
print(dijkstra()[end])