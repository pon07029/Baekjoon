import copy
N = int(input())
li=[list(map(int, input().split())) for _ in range(N)]

def up(arr):
    new = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N-1):
            if new[j][i]==0:
                for k in range(j+1,N):
                    if new[k][i]!=0:
                        new[j][i]=new[k][i]
                        new[k][i]=0
                        break
        for j in range(N-1):
            if new[j][i]!=0 and new[j+1][i]==new[j][i]:
                new[j][i]*=2
                new[j+1][i]=0
        for j in range(N-1):
            if new[j][i]==0:
                for k in range(j+1,N):
                    if new[k][i]!=0:
                        new[j][i]=new[k][i]
                        new[k][i]=0
                        break
    return new

def down(arr):
    new = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N-1,0,-1):
            if new[j][i]==0:
                for k in range(j-1,-1,-1):
                    if new[k][i]!=0:
                        new[j][i]=new[k][i]
                        new[k][i]=0
                        break
        for j in range(N-1,0,-1):
            if new[j][i]!=0 and new[j-1][i]==new[j][i]:
                new[j][i]*=2
                new[j-1][i]=0
        for j in range(N-1,0,-1):
            if new[j][i]==0:
                for k in range(j-1,-1,-1):
                    if new[k][i]!=0:
                        new[j][i]=new[k][i]
                        new[k][i]=0
                        break
    # print(*new, sep='\n')
    return new


def left(arr):
    new = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N-1):
            if new[i][j]==0:
                for k in range(j+1,N):
                    if new[i][k]!=0:
                        new[i][j]=new[i][k]
                        new[i][k]=0
                        break
        for j in range(N-1):
            if new[i][j]!=0 and new[i][j+1]==new[i][j]:
                new[i][j]*=2
                new[i][j+1]=0
        for j in range(N-1):
            if new[i][j]==0:
                for k in range(j+1,N):
                    if new[i][k]!=0:
                        new[i][j]=new[i][k]
                        new[i][k]=0
                        break
    return new

def right(arr):
    new = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N-1,0,-1):
            if new[i][j]==0:
                for k in range(j-1,-1,-1):
                    if new[i][k]!=0:
                        new[i][j]=new[i][k]
                        new[i][k]=0
                        break
        for j in range(N-1,0,-1):
            if new[i][j]!=0 and new[i][j-1]==new[i][j]:
                new[i][j]*=2
                new[i][j-1]=0
        for j in range(N-1,0,-1):
            if new[i][j]==0:
                for k in range(j-1,-1,-1):
                    if new[i][k]!=0:
                        new[i][j]=new[i][k]
                        new[i][k]=0
                        break
    return new

re=[[] for i in range(6)]
re[0].append(li)
for i in range(5):
    for narr in re[i]:
        re[i+1].append(up(copy.deepcopy(narr)))
        re[i+1].append(down(copy.deepcopy(narr)))
        re[i+1].append(left(copy.deepcopy(narr)))
        re[i+1].append(right(copy.deepcopy(narr)))

m=0

for arr in re[5]:
    # print(*arr,sep='\n')
    # print("--------------------")
    for i in range(N):
        for j in range(N):
            if arr[i][j]>m:
                m=arr[i][j]
print(m)

# print(*up(li), sep='\n')
# print("-----------")
# print(*down(li), sep='\n')
# print("-----------")
# print(*left(li), sep='\n')
# print("-----------")
# print(*right(li), sep='\n')