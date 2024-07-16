N=int(input())
arr = [1] * 1000000
end = 1000
for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, 1000000, i): 
            arr[j] = 0
li=[[0]*(N+1) for _ in range(N+1)]
for i in range(2,N+1):
    if arr[int(str(1)+str(i))]==1:
            li[1][i]=1+li[1][i-1]
    else:
        li[1][i]=li[1][i-1]
    if arr[int(str(i)+str(1))]==1:
            li[i][1]=1+li[i-1][1]
    else:
        li[i][1]=li[i-1][1]
li[1][1]=0
for i in range(2,N+1):
    for j in range(2,N+1):
        tmp=0
        if arr[int(str(i)+str(j))]==1:
            tmp=1
        li[i][j]=max(li[i-1][j],li[i][j-1])+tmp
# print(*li, sep='\n')
print(li[-1][-1])


