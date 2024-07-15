import sys
import heapq  
n = int(sys.stdin.readline())
N = int(sys.stdin.readline())
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
  
for i in range(1, n+1):
    if str(i) not in g:
        g[str(i)] = {}


start, ed = map(str, sys.stdin.readline().split())
gl = {no:[] for no in g}
gl[start]=[start]
def dijkstra():
  dis = {no:999999999999 for no in g}
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
        gl[newend] = gl[now] + [newend]
        dis[newend] = total
        heapq.heappush(q, [total, newend]) 
    
  return dis
print(dijkstra()[ed])
print(len(gl[ed]))
print(*gl[ed])