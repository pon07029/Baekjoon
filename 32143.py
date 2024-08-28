import sys
from queue import PriorityQueue
input=sys.stdin.readline
H= int(input())
N, Q= map(int, input().split())
li=list(map(int, input().split()))
q=PriorityQueue()

for i in li:
    q.put(i)
su=sum(li)
if su>=H:
    while su>=H:
        now=q.get()
        su-=now
    q.put(now)
    su+=now
    print(len(q.queue))
else:
    print(-1)

for i in range(Q):
    n=int(input())
    q.put(n)
    su+=n
    if su>=H:
        while su>=H:
            now=q.get()
            su-=now
        q.put(now)
        su+=now
        print(len(q.queue))
    else:
        print(-1)
