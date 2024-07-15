import sys
sys.setrecursionlimit(9999999)
input = sys.stdin.readline
n = int(input())
li = [[]*n for i in range(n+1)]

vi = [0 for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

def f(n):
    for i in li[n]:
        if vi[i] == 0:
            vi[i] = n
            f(i)
f(1)
for i in vi[2:]:
    print(i)
