import sys
from collections import deque
input= sys.stdin.readline
N=int(input())
li=[]
# for i in range(N):
#     li.append(int(input()))
li=list(map(int, input().split()))
s=deque([li[0]])
c=0
for i in li[1:]:
    if s[0]>i:
        c+=len(s)
        s.appendleft(i)
    else:
        c+=len(s)
        while s and s[0]<=i:
            s.popleft()
        s.appendleft(i)
    print(i,s,c)
print(c)