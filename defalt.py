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
import sys
import heapq  
n, M, end = map(int, sys.stdin.readline().split()) 
g={}
for i in range(M):
    a, b, c = map(str, sys.stdin.readline().split())
    if a in g:
        if b in g[a]:
            g[a][b] = min(g[a][b], int(c))
        else:
            g[a][b] = int(c)
    else:
        g[a] = {b:int(c)}
for i in range(1, n+1):
    if str(i) not in g:
        g[str(i)] = {}


def dijkstra(start):
  dis = {str(i): float('inf') for i in range(1, n+1)}
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

###########################프리오더 인오더#######################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(inorder, postorder, in_s, in_e):
    global p_idx
    if in_s > in_e:
        return

    node = Node(postorder[p_idx])
    p_idx -= 1

    index = search(inorder, in_s, in_e, node.value)

    node.right = build_tree(inorder, postorder, index+1, in_e)
    node.left = build_tree(inorder, postorder, in_s, index-1)

    return node

def search(inorder, start, end, target):
    for i in range(start, end+1):
        if inorder[i] == target:
            return i

p_idx = 0
import sys
input = sys.stdin.readline
def main():
    global p_idx
    n=int(input())
    inorder = list(input().split())
    postorder = list(input().split())

    p_idx = n - 1
    root = build_tree(inorder, postorder, 0, n-1)

    preorder_travlesal(root)

def preorder_travlesal(node):
    if node:
        print(node.value, end=" ")
        preorder_travlesal(node.left)
        preorder_travlesal(node.right)


main()

##########################선분 교차 판정########################
def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)
    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
    # 평행
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    # 교차
    else:
        if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
            return 1

    return 0

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

###########################소인수분해#########################
def f(x):
    g={}
    re=1
    while x != 1:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    x = x // i
                    if i in g:
                        g[i] += 1
                    else:
                        g[i] = 1
                    break
            else:
                if x in g:
                        g[x] += 1
                else:
                        g[x] = 1
                break
    for k, v in g.items():
        re *= (k ** v //k*(k-1))
    return re


def prime_factors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i = i + 1
    if n > 1:
        factors.append(n)
    return factors

################################## convex hull ########################################

# monotone chain
def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return c > 0

def convex_hull(positions):
    convex = []
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(*p1, *p2, *p3):
                break
            convex.pop()
        convex.append(p3)

    return len(convex)

n = int(input())
positions = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))
print(convex_hull(positions) + convex_hull(positions[::-1]) - 2)


#graham scan

import sys
from functools import cmp_to_key

N=int(sys.stdin.readline().rstrip())

points=[]
for i in range(N):
    points.append(list(map(int,sys.stdin.readline().rstrip().split())))

points=sorted(points,key=lambda x:(x[1],x[0]))
base=points[0][:]
del points[0]

def cmpccw(a,b): #벡터 base-a, base-b의 외적, ccw:1 cw:-1 0이면 a가 짧으면:1, 길면: -1 반환
    v1=[a[0]-base[0],a[1]-base[1]]
    v2=[b[0]-base[0],b[1]-base[1]]
    if (v1[0]*v2[1])-(v1[1]*v2[0])>0:
        return 1
    elif (v1[0]*v2[1])-(v1[1]*v2[0])<0:
        return -1
    else:
        if (v1[0]**2+v1[1]**2)>(v2[0]**2+v2[1]**2):
            return -1
        else:
            return 1

def ccw(a,b,c,d): #벡터 a-b, c-d의 외적 ccw:1 cw:-1 line:0
    v1=[b[0]-a[0],b[1]-a[1]]
    v2=[d[0]-c[0],d[1]-c[1]]
    if (v1[0]*v2[1])-(v1[1]*v2[0])>0:
        return 1
    elif (v1[0]*v2[1])-(v1[1]*v2[0])<0:
        return -1
    else:
        return 0

points=sorted(points,key=cmp_to_key(cmpccw),reverse=True)

ans=[]
ans.append(base)
ans.append(points[0])
for i in range(1,N-1):
    new=points[i]
    if ccw(ans[-2],ans[-1],ans[-1],new)==1:
        ans.append(new)
        
    elif ccw(ans[-2],ans[-1],ans[-1],new)==-1:
        ans.pop()
        while ccw(ans[-2],ans[-1],ans[-1],new)<=0:
            ans.pop()
        ans.append(new)
        
    elif ccw(ans[-2],ans[-1],ans[-1],new)==0:
        ans.pop()
        ans.append(new)

print(len(ans))
####################################체 #############################
def prime_numbers(n):
    arr = [i for i in range(n+1)] # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i*i, n+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

####################################KMP############################
# KMP 알고리즘을 수행하기 전, 패턴을 처리하는 함수
# 패턴의 테이블 생성
def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)] # 정보 저장용 테이블
    
    pidx = 0 # 테이블의 값을 불러오고, 패턴의 인덱스에 접근
    for idx in range(1, lp): # 테이블에 값 저장하기 위해 활용하는 인덱스
        # pidx가 0이 되거나, idx와 pidx의 pattern 접근 값이 같아질때까지 진행
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = tb[pidx-1]
        
        # 값이 일치하는 경우, pidx 1 증가시키고 그 값을 tb에 저장
        if pattern[idx] == pattern[pidx] :
            pidx += 1
            tb[idx] = pidx
    
    return tb
    
    
def KMP(word, pattern):
    # KMP_table 통해 전처리된 테이블 불러오기
    table = KMP_table(pattern)
    
    results = [] # 결과를 만족하는 인덱스 시점을 기록하는 리스트
    pidx = 0
    
    for idx in range(len(word)):
        # 단어와 패턴이 일치하지 않는 경우, pidx를 table을 활용해 값 변경
        while pidx > 0 and word[idx] != pattern[pidx] :
            pidx = table[pidx-1]
        # 해당 인덱스에서 값이 일치한다면, pidx를 1 증가시킴
        # 만약 pidx가 패턴의 끝까지 도달하였다면, 시작 인덱스 값을 계산하여 추가 후 pidx 값 table의 인덱스에 접근하여 변경
        if word[idx] == pattern[pidx]:
            if pidx == len(pattern)-1 :
                results.append(idx-len(pattern)+2)
                pidx = table[pidx]
            else:
                pidx += 1
    
    return results


#################################세그먼트 트리##############################
# 세그먼트 트리
import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
l = []
segment_tree = [0]*(N*4)

def init(start, end, index):
    if start == end:
        segment_tree[index] = l[start-1]
        return segment_tree[index]
	
    mid = (start+end) // 2
    segment_tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return segment_tree[index]

def find(start, end, index, left, right):
    if start > right or end < left:
        return 0
        
    if start >= left and end <= right:
        return segment_tree[index]

    mid = (start + end) // 2
    sub_sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return sub_sum

def update(start, end, index, update_idx, update_data):
    if start > update_idx or end < update_idx:
        return
    segment_tree[index] += update_data
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2+1, update_idx, update_data)

for _ in range(N):
    l.append(int(input()))

init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        temp = c - l[b-1]
        l[b-1] = c
        update(1, N, 1, b, temp)

    elif a == 2:
        print(find(1, N, 1, b, c))


####################################뤼카 정리#############################
import math
def comb(n,m,p):
    if n<m: 
        print(0)
        exit()
    return math.comb(n,m)%p

def f(n,m,p):
    if n==0 or m==0: return 1
    return comb(n%p,m%p,p)*f(n//p,m//p,p)%p
a,b,c=map(int,input().split())
print(f(a,b,c))


#########################################중국인의 나머지 정리#######################
# Python 3.6
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)  # n 값 모두 곱하기
    for n_i, a_i in zip(n, a):
        p = prod // n_i  # bar n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):  # Modular inverse
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == "__main__":
    n = [3, 5, 7]
    a = [2, 3, 2]
    print(chinese_remainder(n, a))  # 23

    n = [3, 4, 5]
    a = [1, 1, 1]
    print(chinese_remainder(n, a))  # 1


################################밀러 라빈 폴라드 로############################
from math import gcd
from random import randint
from collections import deque
input = sys.stdin.readline

def f(a, n): # 밀러-라빈
    d = n - 1
    r = 0

    while not d % 2:
        d //= 2
        r += 1

    x = pow(a, d, n)
  
    if x == 1 or x == n - 1:
        return True

    for i in range(r-1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True

    return False

def isprime(n):
    if n <= 71:
        if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
            return True
        else:
            return False
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if not f(i, n):
                return False
        return True

def g(x, n, r):
    return (x ** 2 + r) % n

def p(n): #pollard-rho
    if isprime(n):
        return n

    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
        if not n % i:
            return i

    d = 1
    x = randint(2, n)
    y = x
    c = randint(1, n)
    while not d-1:
        y = g(g(y, n, c), n, c)
        x = g(x, n, c)
        t = abs(x - y)
        d = gcd(t, n)

        if d == n:
            return p(n)
    if isprime(d):
        return d
    return p(d)

###########################################LCA##############################

import sys
input = sys.stdin.readline # 시간 초과를 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
LOG = 21 # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프(graph) 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))


################################### 단절점################################
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
