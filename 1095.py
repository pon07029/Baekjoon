import math
S,F,M = map(int,input().split())
co=math.comb(F+S,S)
for i in range(M,0,-1):
    if co%i==0:
        print(i)
        exit()
print(-1)