import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
def f(li):
    global scc_num, idx
    N,M=li[0],li[1]
    graph = [[] for _ in range(2 * N + 1)]
    for i in range(2, 2 * M+1, 2):
        a, b = li[i], li[i + 1]
        graph[-a].append(b)
        graph[-b].append(a)
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
            print(0)
            return
    else:
        print(1)
        return
while True:
    try:
        arr=list(map(int,input().split()))
    except :
        break
    f(arr)
