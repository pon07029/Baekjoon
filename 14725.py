import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input())
pp=[]
for i in range(N):
    li=list(input().split())
    pp.append(li[1:])

def f(n,arr):
    k={}
    for ar in arr:
        if len(ar)==0:
            continue
        if len(ar)==1:
            k[ar[0]]=[]
        if ar[0] not in k:
            k[ar[0]]=[ar[1:]]
        else:
            k[ar[0]].append(ar[1:])

    for k, v in sorted(k.items()):
        if len(v)==0:
            print('--'*n+k)
            continue
        print('--'*n+k)
        f(n+1,v)
f(0,pp)
