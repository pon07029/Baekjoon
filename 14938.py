import heapq  
import sys

n, ran, N= map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
g  = {}
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



def dijkstra(start):
  dis = {str(i): int(ran+1) for i in range(1, n+1)}
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

mx =0
for i in range(n):
   tmp=0
   for j, k in dijkstra(str(i+1)).items():
      if k<=ran:
         tmp+=li[int(j)-1]
   mx=max(mx,tmp)
   
print(mx)