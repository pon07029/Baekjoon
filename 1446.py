import sys
input = sys.stdin.readline
N, D = map(int, input().split())
zi={}
for i in range(N):
    s, e, di = map(int, input().split())
    if s in zi:
        zi[s].append([e, di])
    else :
        zi[s] = [[e, di]]

li = [i for i in range(10001)]

for i in range(D+1):
    if i in zi:
        for j in zi[i]:
            li[j[0]] = min(li[j[0]], li[i]+j[1])

    li[i+1] = min(li[i+1], li[i]+1)

print(li[D])