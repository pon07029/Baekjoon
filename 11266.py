import sys
sys.setrecursionlimit(10**5)
input= sys.stdin.readline


V, E = map(int, input().split())
vi, cnt = [0]*(V+1), [0]
graph = [[]for _ in[0]*(V+1)]
se = set()
def dfs(node, is_root):
      if vi[node]: return
      cnt[0]+=1
      vi[node] = mi = cnt[0]
      visit_cnt = 0
      for child in graph[node]:
        if vi[child]:
          mi = min(mi, vi[child])
        else:
          visit_cnt += 1
          child_cnt = dfs(child, False)
          if not is_root and child_cnt >= vi[node]:
            se.add(node)
          mi = min(mi, child_cnt)
      if is_root and visit_cnt >= 2:
        se.add(node)
      return mi
for _ in range(E):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
for node in range(1, V+1):
		dfs(node, True)
	
print(len(se))
if se: print(*sorted(se))
