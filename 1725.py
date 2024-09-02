import sys
input=sys.stdin.readline
from collections import deque
def f():
    s=deque([])
    N=int(input())
    li=[N]
    for i in range(N):
        li.append(int(input()))
    li.append(0)
    if li[0]==0:
        exit()
    s.append((li[1],1))
    mx=0
    for i in range(2,li[0]+2):
        if s[0][0] <= li[i]:
            s.appendleft((li[i], i))
        else: 
            while s and s[0][0] > li[i]:
                a,b=s.popleft()
                mx=max(mx, a*(i-b))
            s.appendleft((li[i], b))
    print(mx)

f()