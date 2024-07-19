import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N =int(input())
dat=list(map(int, input().split()))
re =[[-1]*N for _ in range(N)]
for i in range(N):
    re[i][i]=1

def f(s,e):
    if s==e:
        return 1
    if s+1==e:
        if dat[s]==dat[e]:
            re[s][e]=1
            return re[s][e]
        re[s][e]=0
        return re[s][e]
    else: 
        if re[s][e]==-1:
            if dat[s]==dat[e]:
                re[s][e]=f(s+1,e-1)
                return re[s][e]
            else:
                re[s][e]=0
                return re[s][e]
        else:
            return re[s][e]

M= int(input())
for i in range(M):
    a,b= map(int, input().split())
    print(f(a-1,b-1))