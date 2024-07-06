#bfs 
import sys
n, m = map(int, input().split())
g  = {}
for i in range(m):
    e, f = map(int, sys.stdin.readline().split())
    if e in g:
        g[e].append(f)
    else:
        g[e] = [f]
    if f in g:
        g[f].append(e)
    else:
        g[f] = [e]


def bfs(start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    number =0
    dep=1
    while need_visited:
        tmp =[]
        tmpp=[]
        for node in need_visited:
            if node not in visited:
                visited.append(node)
                for i in g[node]:
                      tmp.append(i) 
        for i in list(set(tmp)):
            if i not in visited:
                tmpp.append(i)
        number+=len(tmpp)*dep        
        need_visited = tmpp
        dep+=1    
    return number
tmp =bfs(1)
re= 1
for i in range(n):
    k =bfs(i+1)
    if k<tmp:
        tmp = k
        re = i+1
    
print(re)