import sys
N, M = map(int, input().split())
arr= [[0]*(M+1) for _ in range(N+1)]
s=[]

for i in range(1,int(input())+1):
    a,b,c,d = map(int, sys.stdin.readline().split())
    s.append((a,b,c,d))
re=[[0]*(M+1) for _ in range(N+1)]
re[0][0]=1

for i in range(1,M+1):
    if  (0, i ,0 , i-1) in s or  (0, i-1 ,0 , i) in s:
        continue
    re[0][i]=re[0][i-1]

for i in range(1,N+1):
    if  (i, 0 ,i-1 , 0) in s or (i-1, 0 ,i , 0) in s:
        continue
    re[i][0]=re[i-1][0]

for i in range(1,N+1):
    for j in range(1,M+1):
        if ((i, j, i-1,j ) in s or (i-1,j,i,j) in s )==False :
            re[i][j]+=re[i-1][j]
        if ((i, j, i,j-1 ) in s or (i,j-1,i,j) in s )==False:
            re[i][j]+=re[i][j-1]

print(re[-1][-1])
            