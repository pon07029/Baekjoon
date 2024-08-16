import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def f():
    global scc_num, idx
    N,M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(2 * N + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[-a].append(b)
        graph[-b].append(a)
    graph[-1].append(1)
    scc_num = 1
    idx = 1
    stack = []
    scc_idx = [0] * (2 * N + 1)
    check = [0] * (2 * N + 1)
    visit = [0] * (2 * N + 1)
    def SCC(node):
        global idx, scc_num
        visit[node] = idx
        root = idx
        idx += 1
        stack.append(node)
        for nxt in graph[node]:
            if not visit[nxt]:
                root = min(root, SCC(nxt))
            elif not check[nxt]:
                root = min(root, visit[nxt])
        if root == visit[node]:
            while stack:
                top = stack.pop()
                check[top] = 1
                scc_idx[top] = scc_num
                if node == top:
                    break
            scc_num += 1
        return root
    for i in range(1, N + 1):
        if not visit[i]:
            SCC(i)
    for i in range(1, N + 1):
        if scc_idx[i] == scc_idx[-i]:
            print("no")
            return
    else:
        print("yes")
while True:
    try:
        f()
    except:
        break

