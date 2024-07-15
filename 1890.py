import sys
N = int(input())
li=[]
arr = [[0]*N for i in range(N)]
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
arr[0][0]=1

for k in range(N):
    for i in range(0,k+1):
        j= k-i
        if arr[i][j]!=0:
            m=li[i][j]
            if i+m<N:
                arr[i+m][j]+=arr[i][j]
            if j+m<N:
                arr[i][j+m]+=arr[i][j]



for k in range(N, 2*N-2):
    for i in range(k-N+1, N):
        j = k-i
        if arr[i][j]!=0:
            m=li[i][j]
            if i+m<N:
                arr[i+m][j]+=arr[i][j]
            if j+m<N:
                arr[i][j+m]+=arr[i][j]
print(arr[-1][-1])
        