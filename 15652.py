
def fun(start, end, n):
    le =[]
    if n == 1:
        return [[i] for i in range(start, end+1)]
    for i in range(start, end+1):
        for j in fun(i, end, n-1):
            le.append([i]+j)
    return le
a, b=map(int, input().split())
for i in fun(1, a,b ):
    print(*i)