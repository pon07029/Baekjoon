import sys
from functools import cmp_to_key
import math
input=sys.stdin.readline
def f():
    N=int(sys.stdin.readline().rstrip())
    points=[]

    for i in range(math.ceil(N/5)):
        lis=list(map(int,sys.stdin.readline().rstrip().split()))
        for i in range(0,len(lis),2):
            points.append([lis[i],lis[i+1]])
 
    def ccw(x1, y1, x2, y2, x3, y3):
        c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        return c > 0

    def convex_hull(positions):
        convex = []
        for p3 in positions:
            while len(convex) >= 2:
                p1, p2 = convex[-2], convex[-1]
                if ccw(*p1, *p2, *p3):
                    break
                convex.pop()
            convex.append(p3)

        return convex

    positions = sorted(points, key=lambda x: (-x[1], x[0]))
    convex1 = convex_hull(positions)
    convex2=convex_hull(positions[::-1])
    convex1.pop(0)
    convex1.pop(-1)
    print(len(convex1)+len(convex2))
    for i in convex2[::-1]:
        print(i[0], i[1])
    for i in convex1[::-1]:
        print(i[0], i[1])
T=int(input())
for i in range(T):
    f()