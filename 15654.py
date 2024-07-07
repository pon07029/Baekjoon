import sys
a, b=map(int, input().split())

dat = list(map(int, sys.stdin.readline().split()))
dat.sort()
def fun(arr, n):
    le =[]
    if n == 1:
        return [[i] for i in arr]
    for i in arr:
        k = arr[:]
        k.remove(i)
        for j in fun(k, n-1):
            le.append([i]+j)
    return le

for i in fun(dat, b):
    print(*i)