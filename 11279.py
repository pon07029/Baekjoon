#힙
import sys
import heapq
q =[]
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        if q:
            print(-1*heapq.heappop(q))
        else:
            print(0)
    else :
        heapq.heappush(q, -1*a)