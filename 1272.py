import sys
input = sys.stdin.readline
N, R = map(int, input().split())
dat = list(map(int, input().split()))
for i in range(N):
    if i==R-1: continue
    dat[i]-=dat[R-1]
ch=[False]*(N+1)
li=[-1 for i in range(N+1)]
g={}
for i in range(N-1):
    a, b = map(int, input().split())
    if a in g:
        g[a].append(b)
    else:
        g[a]=[b]
    if b in g:
        g[b].append(a)
    else:
        g[b]=[a]
ch[R]=True
def f(n):
    if li[n]!=-1:
        return li[n]
    tmp=0
    for i in g[n]:
        if ch[i]: continue
        ch[i]=True
        tmp+=f(i)
    li[n]=tmp
    # print(n,tmp)
    return li[n]+1
f(R)
# print(*li)
# print(dat)
# print(sum(dat))
mx=0
for i in range(N):
    if i==R-1: continue
    mx=max(mx,dat[i]*li[i+1])
print(sum(dat)-mx+dat[R-1])