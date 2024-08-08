import math
import sys
input=sys.stdin.readline
N=int(input())

def f(x):
    g={}
    re=1
    while x != 1:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    x = x // i
                    if i in g:
                        g[i] += 1
                    else:
                        g[i] = 1
                    break
            else:
                if x in g:
                        g[x] += 1
                else:
                        g[x] = 1
                break
    for k, v in g.items():
        re *= (2*v + 1)
        re-=v
    return re
for i in range(N):
    print(f"Scenario #{i+1}:")
    print(f(int(input())))
    print()