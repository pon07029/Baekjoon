import sys
input=sys.stdin.readline
N,K=map(int,input().split())
dia=[]
total=0
for _ in range(N):
    dia.append(tuple(map(int,input().split())))
dia.sort(key=lambda x: (-x[1], -x[0]))
bag=[]
for _ in range(K):
    bag.append(int(input()))
bag.sort(reverse=True)
start=0
for i in bag:
    for j in range(start,N):
        m,v=dia[j]
        if i>=m:
            total+=v
            start=j+1
            break
print(total)

