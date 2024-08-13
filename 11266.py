import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
visit_order = [0]*(V+1)
answer = set()
edge_dict = defaultdict(list)
for _ in range(E) :
  a, b = map(int, input().split())
  edge_dict[a].append(b)
  edge_dict[b].append(a)

def dfs(node, isroot) :
  visit_order[0]+=1
  visit_order[node] = visit_order[0]
  child_num = 0
  child_order = visit_order[node]
  
  for nxt in edge_dict[node] :
    if visit_order[nxt] :
      child_order = min(child_order, visit_order[nxt])
    else :
      child_num += 1
      tmp = dfs(nxt, False)
      if not isroot and tmp >= visit_order[node] :
        answer.add(node)
      child_order = min(child_order, tmp)
      
  if isroot and child_num >= 2 :
    answer.add(node)
  return child_order

for i in range(1,V+1) :
  if visit_order[i] ==0 :
    dfs(i, True)
answer = sorted(list(answer))
print(len(answer))
print(*answer)
