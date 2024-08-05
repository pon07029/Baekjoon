a, b = map(int, input().split())
def f(n):
    if n==0:
        return 0
    n+=2
    two =[]
    while n>0:
        two.append(n%2)
        n//=2
    li=[]
    now = [[1,0],[0,1]]
    ff =[[1,1],[1,0]]
    li.append(ff)
    def solution(arr1, arr2):
        return [[sum(i*j%1000000000 for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1]
    for i in range(len(two)-1):
        li.append(solution(li[-1], li[-1]))
    for i in range(len(two)):
        if two[i]:
            now = solution(now, li[i])

    return now[0][1]-1
print((f(b)-f(a-1))%1000000000)

