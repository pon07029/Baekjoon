import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
visit_order = [0]*(V+1)
answer = []
edge_dict = defaultdict(list)
for _ in range(E) :
  a, b = map(int, input().split())
  edge_dict[a].append(b)
  edge_dict[b].append(a)

def dfs(node, parent) :
  visit_order[0]+=1
  visit_order[node] = visit_order[0]
  child_order = visit_order[node]
  
  for nxt in edge_dict[node] :
    if nxt == parent :
      continue
    if visit_order[nxt] :
      child_order = min(child_order, visit_order[nxt])
      continue
    
    tmp = dfs(nxt, node)
    child_order = min(child_order, tmp)
    if tmp > visit_order[node] :
        answer.append(tuple(sorted([node, nxt])))
  return child_order

dfs(1, 0)
re=answer.sort(key=lambda x:(x[0],x[1]))
print(len(answer))
for a,b in answer:
    print(a,b)