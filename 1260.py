import sys
## DFS와 BFS
def dfs_recursive(graph, start, visited = []):
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

a, b, c= map(int, input().split())
g  = {}
for i in range(b):
    e, f = map(int, sys.stdin.readline().split())
    if e in g:
        g[e].append(f)
    else:
        g[e] = [f]
    if f in g:
        g[f].append(e)
    else:
        g[f] = [e]

for i in g:
    g[i].sort()
if c not in g:
    g[c] = []
print(*dfs_recursive(g, c))
print(*bfs(g, c))