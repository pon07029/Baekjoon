import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, b = map(int, sys.stdin.readline().split())
g  = {}
li = [i+1 for i in range(n)]
re =0
def dfs_recursive(graph, start, visited = []):
    visited.append(start)
    li.remove(start)
    if start not in graph:
        return visited
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

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
while li:
    re += 1
    dfs_recursive(g, li[0])

print(re)