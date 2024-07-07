import sys
def f():
    n = int(input())
    li=[]
    for i in range(2):
        li.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, n):
        if i == 1:
            li[0][i]+=li[1][0]
            li[1][i]+=li[0][0]
        else:
            li[0][i]+=max(li[0][i-2], li[1][i-2], li[1][i-1])
            li[1][i]+=max(li[0][i-2], li[1][i-2], li[0][i-1])

    print(max(li[0][n-1], li[1][n-1], li[0][n-2], li[1][n-2]))

for i in range(int(input())):
    f()
