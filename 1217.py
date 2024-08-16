import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import collections
def f():
    global id
    e,v = map(int, input().split())
    if e==0 and v==0:
        exit()
    graph = collections.defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        aa=a+v
        bb=b+v
        if a<0:
            aa=-a
            a = v-a
        if b<0:
            bb=-b
            b = v-b
        graph[aa-1].append(b-1)
        graph[bb-1].append(a-1)
    v=v*2
    d = [-1 for _ in range(v)]
    stack=[]
    on_stack=[False for _ in range(v)]
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

    for i in range(v):
        if d[i] ==-1: #방문 이력이 없는 노드
            dfs(i)
    re.sort(key=lambda x:x[0])
    # print(len(re))
    v=v//2
    for arr in re:
            g={}
            for i in arr:
                tmp = i if i<=v else i-v
                if tmp in g:
                    print("0")
                    return
                g[tmp]=1
    print("1")
while True:
    f()

