import sys
input = sys.stdin.readline
N=int(input())
M=int(input())
li=list(map(int,input().split()))
arr=[list(map(int,input().split())) for _ in range(M)]
people=[0]*N
for i in range(len(li)):
    target=li[i]
    for j in range(N):
        if arr[i][j]==target:
            people[j]+=1
        else:
            people[target-1]+=1
print(*people, sep='\n')