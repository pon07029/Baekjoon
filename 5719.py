import sys
import heapq 
def f(): 
    n, M = map(int, sys.stdin.readline().split()) 
    if n==0 and M==0:
        exit()
    s,e =map(int, sys.stdin.readline().split())
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
    for i in range(n):
        if str(i) not in g:
            g[str(i)] = {}

    def dijkstra(start):
        dis = {str(i): 600000 for i in range(n)}
        dis[start] = 0 
        q = []
        heapq.heappush(q, [dis[start], start])  

        while q:  
            nowdis, now = heapq.heappop(q) 

            if dis[now] < nowdis: 
                continue
            for newend, newdis in g[now].items():
                total = nowdis + newdis  
                if total < 600000:
                    if total < dis[newend]: 
                        dis[newend] = total
                        heapq.heappush(q, [total, newend]) 
        
        return dis

    totalCost = dijkstra(str(s))[str(e)]
    if totalCost == 600000:
        print(-1)
        return
    save=[]
    def DFS(start,cost, arr):
        if start==str(e) and cost == totalCost:
            save.append(arr)
            return
        for i in g[start]:
            if g[start][i]+cost<=totalCost:
                if i not in arr:
                    DFS(i,g[start][i]+cost,arr+[i])
        return
    DFS(str(s),0,[str(s)])
    for arr in save:
        l=len(arr)
        for i in range(1,l):
            st=arr[i-1]
            et=arr[i]
            if st!=et:
                g[st][et]=600000
    tt=dijkstra(str(s))[str(e)]
    if tt==600000:
        print(-1)
        return
    else:
        print(tt)
while True:
    f()