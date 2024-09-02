import sys
import copy
input=sys.stdin.readline
N, M= map(int, input().split())
c=list(map(int, input().split()))
peo=[0]*(N+1)
party={}
re=0
for i in range(N):
    peo[i+1]=i+1
    if c[i]%2==0:
        party[i+1]=(1,0)
    else:
        party[i+1]=(0,1)
for _ in range(M):
    a, b = map(int, input().split())
    if peo[a] == peo[b]:
        print(re)
        continue
    p1, p2 = peo[a], peo[b]
    re-=(party[p1][0]*party[p1][1])+(party[p2][0]*party[p2][1])
    peo[b] = peo[a]
    plus =(party[p1][0]+party[p2][0], party[p1][1]+party[p2][1])
    party[p1] = plus
    party.pop(p2)
    # party[p2] = plus
    re+=(party[p1][0]*party[p1][1])
    print(re)
    print(party)
    print(peo)