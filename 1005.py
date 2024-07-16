import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def ff():
    N, K =  map(int, input().split())
    dat = list(map(int, input().split()))
    tim = [-1]*(N+1)
    g={}
    for i in range(K):
        a,b = map(int, input().split())
        if b in g:
            g[b].append(a)
        else:
            g[b]=[a]
    for i in range(1,N+1):
        if i not in g:
            tim[i] = dat[i-1]
            g[i]=[]

    E = int(input())

    def f(end):
        if tim[end] != -1:
            return tim[end]
        elif g[end]:
            for i in g[end]:
                tim[end] = max(tim[end], f(i)+dat[end-1])
            return tim[end] 
        else:
            return tim[end]
    print(f(E))
    
for _ in range(int(input())):
    ff()
