import sys
input=sys.stdin.readline
li=[-1]*101


def f(p):
    if p>=100:
        return f(p%100)+f(p//100)

    if p<0:
        return 9999999
    if p==0:
        return 0
    if p==1:
        return 1
    if li[p]!=-1:
        return li[p]

    li[p]=min(f(p-1)+1,f(p-25)+1,f(p-10)+1)
    return li[p]




for i in range(int(input())):
    print(f(int(input())))
    