#힙
#튜플
import sys
import heapq
q =[]
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else :
        heapq.heappush(q, (abs(a),a))