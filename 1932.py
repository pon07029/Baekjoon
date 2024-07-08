import sys
n= int(sys.stdin.readline())
li=[]
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            li[i][j] += li[i-1][j]
        elif j == i:
            li[i][j] += li[i-1][j-1]
        else:
            li[i][j] += max(li[i-1][j-1], li[i-1][j])
print(max(li[n-1]))