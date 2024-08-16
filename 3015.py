import sys
from collections import deque
input= sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    li.append(int(input()))
# li=list(map(int, input().split()))
N,c,tmp=len(li),0,1
s=deque([li[0]])
count=deque([1])
for i in range(1,N):
    if li[i]>li[i-1]:
        while s and s[-1]<li[i]:
            s.pop()
            c+=count.pop()
        if s and s[-1]==li[i]:
            c+=count[-1]
            count[-1]+=1
        else:
            s.append(li[i])
            count.append(1)
        if len(s)>1:
            c+=1
    elif li[i]<li[i-1]:
        s.append(li[i])
        count.append(1)
        c+=1
    else:
        c+=count[-1]
        count.append(count.pop()+1)
        if len(s)>1:
            c+=1
print(c)

