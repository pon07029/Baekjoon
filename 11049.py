N=int(input())
li=[(1,1)]*N
for i in range(N):
    a,b=map(int,input().split())
    li[i]=(a,b)
dp=[[0]*N for _ in range(N)]



print(f(0,N-1))
