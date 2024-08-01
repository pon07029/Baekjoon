D=int(input())
arr=[[0 for i in range(8)] for _ in range(8)]
road=[(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6),(5,7),(6,8),(7,8)]
for i,j in road:
    arr[i-1][j-1]=arr[j-1][i-1]=1

li=[]
def solution(arr1, arr2):
    return [[sum(i*j for i, j in zip(row, col))%1000000007 for col in zip(*arr2)] for row in arr1]
re=[]
re.append(arr)
while D:
    if D%2:
        li.append(1)
    else:
        li.append(0)
    D//=2
arr2=[[0 for i in range(8)] for _ in range(8)]
for i in range(8):
    arr2[i][i]=1

for i in range(len(li)):
    re.append(solution(re[-1], re[-1]))
for i in range(len(li)):
    if li[i]:
        arr2=solution(arr2, re[i])
print(arr2[0][0])