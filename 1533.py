import sys
N, S, E, T= map(int, sys.stdin.readline().split())
li=[[0]*(N*5) for i in range(N*5)]
for i in range(N):
    for j in range(4):
        li[i*5+j+1][i*5+j]=1
ar=[list(input()) for i in range(N)]
for i in range(N):
    for j in range(N):
        num=str(ar[i][j])
        if num:
            li[i*5][j*5+int(num)-1]=1

def solution(arr1, arr2):
    return [[sum(i*j for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1]

