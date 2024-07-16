import sys
import math
input = sys.stdin.readline
N, M, C = map(int, input().split())
li=[]
mp=[[0]*M for i in range(N)]
for i in range(C):
    a, b = map(int, input().split())
    mp[a-1][b-1]=1
mpp=[]
for i in range(C+2):
    ar=[[0]*M for i in range(N)]
    mpp.append(ar)

now=0
for i in range(N):
    if mp[i][0]:
        now+=1
    mpp[now][i][0]=1
now = 0
for i in range(M):
    if mp[0][i]:
        now+=1
    mpp[now][0][i]=1

for i in range(1,N):
    for j in range(1,M):
        kk=mp[i][j]
        for k in range(C+1):
            # print(i,j,k,kk)
            mpp[k+kk][i][j]= mpp[k][i-1][j]+mpp[k][i][j-1]
            mpp[k+kk][i][j]%=1000000007

for i in range(C+2):
    print(*mpp[i], sep='\n')
    print("")
for i in range(C+1):
    print(mpp[i][-1][-1], end=' ')


