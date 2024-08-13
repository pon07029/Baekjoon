import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
arr=list(map(int,input().split()))
mx=0
for i in range(M-1):
    mx=max(mx,(arr[i+1]-arr[i]+1)//2)
mx=max(mx,arr[0]-0,N-arr[-1])
print(mx)