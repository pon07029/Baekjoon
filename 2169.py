import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li=[list(map(int, input().split())) for _ in range(N)]
re=[[-999999999]*M]
re[0][0]= li[0][0]
for i in range(1, M):
    re[0][i]=re[0][i-1]+li[0][i]

for i in range(1,N):
    t1=[re[i-1][0]+li[i][0]]
    for j in range(1,M):
        t1.append(max(t1[-1], re[i-1][j])+li[i][j])
    t2=[0]*M
    t2[M-1]= re[i-1][M-1]+li[i][M-1]
    for j in range(M-2, -1, -1):
        t2[j]=(max(t2[j+1], re[i-1][j])+li[i][j])
    # print(re[i-1])
    # print(t1)
    # print(t2)
    # print("")
    tmp=[max(t1[j], t2[j]) for j in range(M)]
    re.append(tmp)

# print(*re, sep="\n")

print(re[N-1][M-1])
