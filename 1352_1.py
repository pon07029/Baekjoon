import sys
input=sys.stdin.readline
N, X, Y = map(int, sys.stdin.readline().split())
li=list(map(int, sys.stdin.readline().split()))
re=0
ree=0
for l in li:
    na=l%X
    mo=l//X
    if na>mo*(Y-X):
        na-=mo*(Y-X)
    else:
        na=0
    # print(l, na, mo)
    re+=mo
    ree+=na
print(re)
print(ree)
