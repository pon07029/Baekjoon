def solution(arr1, arr2):
    return [[sum(i*j for i, j in zip(row, col))%1000 for col in zip(*arr2)] for row in arr1]
import sys
N, X = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
li=[]
le=[arr]
b=X
are = [[1 if i==j else 0 for i in range(N)] for j in range(N)]
while True:
    a =b%2
    b =b//2
    li.append(a)
    if b ==0:
        break

for i in range(1,len(li)):
    le.append(solution(le[i-1],le[i-1]))

for i in range(len(li)):
    if li[i]==1:
        are = solution(are,le[i])
for i in range(N):
    print(*are[i])

