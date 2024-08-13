import sys
from collections import deque
def f():
    s=deque([])
    li=list(map(int, input().split()))
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
while True:
     f()