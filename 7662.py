import heapq
import sys

for _ in range(int(input())):
    maxx = []
    minn = []
    n=int(input())
    de=[False]*n
    for i in range(n):
        a, b = map(str, sys.stdin.readline().split())
        b= int(b)
        
        if a == "I":
            heapq.heappush(minn,(b,i))
            heapq.heappush(maxx,(-b,i))
        else:
            if b == 1:
                while maxx and de[maxx[0][1]]:
                    heapq.heappop(maxx)
                if maxx:
                    de[maxx[0][1]]=True
                    heapq.heappop(maxx)
            else:
                while minn and de[minn[0][1]]:
                    heapq.heappop(minn)
                if minn:
                    de[minn[0][1]]=True
                    heapq.heappop(minn)

    while maxx and de[maxx[0][1]]:
        heapq.heappop(maxx)
    while minn and de[minn[0][1]]:
        heapq.heappop(minn)


    if not minn: 
        print("EMPTY")
    else:
        print(-maxx[0][0],minn[0][0]) 