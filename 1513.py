import sys
import math
input = sys.stdin.readline
N, M, C = map(int, input().split())
li=[]
mp=[[0]*M for i in range(N)]
for i in range(C):
    a, b = map(int, input().split())
    mp[a-1][b-1]=i+1
# (가짓수, 마지막 통과, 통과한거 개수)
mpp=[[[[ 0 for k in range(M+1)] for i in range(N+1)] for _ in range(C+1)]for l in range(C+1)]

def f(n,m,l,c):
    if n<1 or m<1:
        return 0
    if mpp[l][c][n][m]:
        return mpp[l][c][n][m]
    if n==1 and m==1:
        if mp[0][0]==0:
            if c==0:
                mpp[l][c][n][m]=1
                return 1
            else:
                mpp[l][c][n][m]=0
                return 0
        if c==1 and mp[0][0] and l >mp[0][0]:
            print(n,m,l,c)
            mpp[l][c][n][m] =1
            return 1
        mpp[l][c][n][m]=0
        return 0
    if mp[n-1][m-1]:
        if l>=mp[n-1][m-1]:
            mpp[l][c][n][m]= (f(n, m-1, mp[n-1][m-1], c-1)+f(n-1, m, mp[n-1][m-1], c-1))%1000007
            return mpp[l][c][n][m]
        else:
            mpp[l][c][n][m] =0
            return 0
    mpp[l][c][n][m] = (f(n, m-1, l, c)+ f(n-1, m, l, c))%1000007
    return mpp[l][c][n][m]

for i in range(C+1):
    print(f(N,M,C,i), end=" ")



