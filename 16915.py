import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import collections
def f():
    global id
    v,e = map(int, input().split())
    v=2*v
    graph = [[] for _ in range(v+1)]
    init=list(map(int, input().split()))
    for _ in range(e):
        l=list(map(int, input().split()))
        ass=l[1]
        graph[ass]=list(set(graph[ass])| set(l[1:]))
        graph[-ass]=list(set(graph[ass])| set(l[1:]))
    print(graph)
    d = [-1 for _ in range(v+1)]
    stack=[]
    on_stack=[False for _ in range(v+1)]
    id=0
    re=[]
    def dfs(cur):
        global id
        id +=1
        d[cur] = id
        stack.append(cur)
        on_stack[cur] = True
        
        parent = d[cur]
        for next in graph[cur]:
            if d[next]==-1: #방문 이력이 없는 노드
                parent= min(parent, dfs(next))
            elif on_stack[next]: #방문 체크는 되어있지만 아직 처리 완료 X
                parent = min(parent, d[next])

        if parent == d[cur]: #자신과 부모가 동일
            scc = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                scc.append(node+1) #인덱스를 다시 숫자로 변환
                if cur == node:
                    break
            scc.sort()
            re.append(scc)
        return parent

    for i in range(1,v+1):
        if d[i] ==-1: #방문 이력이 없는 노드
            dfs(i)
    re.sort(key=lambda x:x[0])
    # print(len(re))
    for arr in re:
            print(arr)
    print("1")
f()

