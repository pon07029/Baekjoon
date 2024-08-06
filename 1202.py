import sys
import heapq
input=sys.stdin.readline
N,K=map(int,input().split())
li=[]
dia=[]
total=0
dia=[tuple(map(int,input().split())) for _ in range(N)]
dia.sort()
bag=[int(input()) for _ in range(K)]
bag.sort()
for i in bag:
    while dia and dia[0][0]<=i:
        heapq.heappush(li,-dia[0][1])
        heapq.heappop(dia)
    if li:
        total+=-heapq.heappop(li)
print(total)

