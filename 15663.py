import sys
a, b=map(int, input().split())

dat = list(map(int, sys.stdin.readline().split()))
dat.sort()
num=[]
visited=[False]*a
def fun():
    if len(num) == b:
        print(*num)
        return
    last =0
    for i in range(a):
        if visited[i] or last == dat[i]:
            continue
        last = dat[i]
        visited[i] = True
        num.append(dat[i])
        fun()
        visited[i] = False
        num.pop()
fun()
