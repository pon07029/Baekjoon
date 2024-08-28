import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = [-1] * N
B = [-1] * M
graph = [[] for _ in range(N)]
match = [False]*N
for i in range(N):
    cow = list(map(int,input().split()))
    for j in range(1,cow[0]+1):
        graph[i].append(cow[j]-1)

def bipartite(a):
    if match[a]:
        return False
    match[a] = True
    for b in graph[a]:
        if B[b] == -1:
            A[a] = b
            B[b] = a
            return True
    for b in graph[a]:
        if bipartite(B[b]):
            A[a] = b
            B[b] = a
            return
    return False

count = 0
for i in range(N):
    if A[i] == -1:
        match = [False]*N
        if bipartite(i): count += 1
    if count == M: break

print(count)