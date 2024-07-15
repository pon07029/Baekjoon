#웜홀
import sys
input = sys.stdin.readline
INF = int(1e9)
def f():
    v, e, d = map(int, input().split())
    ed = []
    dis = [1e9] * (v + 1)


    for _ in range(e):
        a, b, c = map(int, input().split())
        ed.append((a, b, c))
        ed.append((b, a, c))
    for _ in range(d):
        a, b, c = map(int, input().split())
        ed.append((a, b, -c))

    def bf():
        for i in range(v):
            for j in range(len(ed)):
                cur, ne ,co = ed[j]

                if dis[ne] > dis[cur] + co:
                    dis[ne] = dis[cur] + co
                    if i == v - 1:
                        return True
        return False


    if bf():
        print("YES")
    else:
        print("NO")

for i in range(int(input())):
    f()