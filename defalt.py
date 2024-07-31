##############################입력###############################
a = input()
a = int(input())
a= int(sys.stdin.readline())

a, b= map(int, input().split())
a, b = map(int, sys.stdin.readline().split())

dat = list(map(int, input().split()))
dat = list(map(int, sys.stdin.readline().split()))  
print(max(map(max,re)))


data = [input().strip() for i in range(int(input()))]
data = [sys.stdin.readline().strip() for i in range(int(input()))]

import sys
sys.setrecursionlimit(10**6)

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(b//(a+1))
    except EOFError:
        break


while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break



a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

re=[]
for i in range(int(input())):
  a= int(sys.stdin.readline())
  re.append(a)

##############################출력##############################

print(*li)
print(*re, sep="\n")

li = [0 for i in range(26)]

for i in range(int(input()),0,-1):
    print(i)


if a == "011":
    print("")
elif a == "016":
    print("")
elif a == "019":
    print("")
else:
    print("")


''.join([i * n for i in my_string])

string.count(str(i))



###################################정렬###########################

re = sorted(re, key=len)
re = sorted(re, reverse = True)

data.sort(key=lambda x : int(x[0]))
data.sort(key=lambda x : (x[0], x[1]))

# 딕셔너리의 값들만 추출
values = list(dic.values())


##############################딕셔너리##############################
dat.count(a)
for key, value in dic.items():
    print(f'{key}\n'*value, end="")



#################################기타함수####################################

def binary_search(target, data):
    data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return
# 사잇값
def binary_search(target, start,end):

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if li[mid] == target:
            return mid 

        elif li[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return  start   


def sosu(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res


  li[a-1], li[b-1] = li[b-1], li[a-1]


def lcm(a, b):
    return a * b / math.gcd(a, b)

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def is_prime_number(n):
    array = [True for i in range(n+1)] 

    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]
#######################그래프#################


a, b, c= map(int, input().split())
g  = {}
for i in range(b):
    e, f = map(int, sys.stdin.readline().split())
    if e in g:
        g[e].append(f)
    else:
        g[e] = [f]
    if f in g:
        g[f].append(e)
    else:
        g[f] = [e]





from collections import deque
def dfs2(graph, start_node):    
    visited = []
    need_visited = deque()

    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
 
        if node not in visited:
 
            visited.append(node)
            need_visited.extend(graph[node])
                
    return visited

def dfs_recursive(graph, start, visited = []):
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

#######################dfs#################
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)
#######################dfs#################


import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
day = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            que.append((i, j))

def bfs():
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))

bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()
        day = max(day,graph[i][j])
print(day-1)

#######################다익스트라########################
g={}
for i in range(N):
    a, b, c = map(str, sys.stdin.readline().split())
    if a in g:
        if b in g[a]:
            g[a][b] = min(g[a][b], int(c))
        else:
            g[a][b] = int(c)
    else:
        g[a] = {b:int(c)}
    if b in g:
        if a in g[b]:
            g[b][a] = min(g[b][a], int(c))
        else:
            g[b][a] = int(c)
    else:
        g[b] = {a:int(c)}
for i in range(1, n+1):
    if str(i) not in g:
        g[str(i)] = {}
import heapq  

def dijkstra(g, start):
  dis = {no for no in g}
  dis[start] = 0 
  q = []
  heapq.heappush(q, [dis[start], start])  

  while q:  
    nowdis, now = heapq.heappop(q) 

    if dis[now] < nowdis: 
      continue
    
    for newend, newdis in g[now].items():
      total = nowdis + newdis  
      if total < dis[newend]: 
        dis[newend] = total
        heapq.heappush(q, [total, newend]) 
    
  return dis

####################BAG################################
def main():
    n, k = map(int, input().split())
    k += 1

    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        tmp = {}
        for v_bag, w_bag in bag.items():
            if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
                tmp[nv]=nw
        bag.update(tmp)

    print(max(bag.keys()))

main()


n, k = map(int, input().split())
lst=[[0, 0]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[n][k])
##########################벨만 포드##########################
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
ed = []
dis = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    ed.append((a, b, c))


def bellman_ford(start):
    dis[start] = 0
    for i in range(v):
        for j in range(e):
            cur = ed[j][0]
            ne = ed[j][1]
            co = ed[j][2]
            if dis[cur] != INF and dis[ne] > dis[cur] + co:
                dis[ne] = dis[cur] + co
                if i == v - 1:
                    return True
    return False


re = bellman_ford(1)

if re:
    print("-1")
else:
    for i in range(2, v + 1):
        if dis[i] == INF:
            print("-1")
        else:
            print(dis[i])

##############################행렬곱######################
def solution(arr1, arr2):
    return [[sum(i*j for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1]

#############################외판원###########################
import sys
N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
dp = {}
def f(now, vi):
    if vi == (1 << N) - 1:
        if li[now][0]:
            return li[now][0]
        else:
            return int(1e9)
    if (now, vi) in dp:
        return dp[(now, vi)] 
    mi = int(1e9)
    for next in range(1, N):
        if li[now][next] == 0 or vi & (1 << next):
            continue
        cost = f(next, vi | (1 << next)) + li[now][next]
        mi = min(cost, mi)

    dp[(now, vi)] = mi 
    return mi  
print(f(0, 1))  

def ff(c):
    t=0
    for i in range(N):
        if c & (1 << i):
            t+=1
    return t

##########################스패닝 트리 ########################

import sys
input=sys.stdin.readline
V, E=map(int,input().split())
p=[i for i in range(V+1)]
edges=[]
re=0
for _ in range(E):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()

def fp(x):
    if p[x]==x:
        return x
    p[x]=fp(p[x])
    return p[x]

def up(a,b):
    a=fp(a)
    b=fp(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

for edge in edges:
    c,a,b=edge
    if fp(a)!=fp(b):
        up(a,b)
        re+=c
print(re)

#########################위상 정렬#########################
import sys
from collections import deque
input=sys.stdin.readline
N, M = map(int,input().split())
li=[0 for _ in range(N+1)]
g=[[]for _ in range(N+1)]   
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    li[b]+=1
q=deque([])
for i in range(1,N+1):
    if li[i]==0:
        q.append(i)

re=[]
while q:
    x=q.popleft()
    re.append(x)
    for i in g[x]:
        li[i]-=1
        if li[i]==0:
            q.append(i)

print(*re)