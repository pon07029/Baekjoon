import sys
from queue import PriorityQueue
from collections import deque
input = sys.stdin.readline
N=int(input())
li=[]
sa=[]
q=PriorityQueue()
for i in range(N):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    li.append((a,b))
    sa.append(b)
li.sort(key=lambda x:x[1])
ll=deque(li)
L=int(input())
sa=list(set(sa))
sa.sort()
mx=0
# print(ll)
for i in sa:
    # print(i)
    while ll and ll[0][1]<=i and ll[0][1]>=i-L:
        q.put(ll.popleft()[0])
    # print(q.queue)
    while q.qsize() and q.queue[0]<i-L:
        q.get()
    mx=max(mx,len(q.queue))
print(mx)
