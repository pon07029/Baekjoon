import sys
input=sys.stdin.readline
N=int(input())
g={}
re={}
li=list(map(int, input().split()))
lii=list(map(int, input().split()))
for i in range(N):
    g[li[i]]=i
for i in range(N):
    ii=g[lii[i]]
    if ii-i>=0:
        if ii-i in re:
            re[ii-i].append(lii[i])
        else:
            re[ii-i]=[lii[i]]
mx=max(re.keys())
print(*re[mx])