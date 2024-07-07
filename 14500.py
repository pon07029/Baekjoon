import sys
N, M = map(int, sys.stdin.readline().split())

arr =[list(map(int, sys.stdin.readline().split())) for i in range(N)]

def a(x,y):
    if x+3<N and y<M:
        return arr[x][y]+arr[x+1][y]+arr[x+2][y]+arr[x+3][y]
    return 0

def b(x,y):
    if x<N and y+3<M:
        return arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x][y+3]
    return 0

def c(x,y):
    if x+1<N and y+1<M:
        return arr[x][y]+arr[x+1][y]+arr[x][y+1]+arr[x+1][y+1]
    return 0

def d(x,y):
    if x+2<N and y+1<M:
        return arr[x][y]+arr[x+1][y]+arr[x+2][y]+arr[x][y+1]
    return 0

def e(x,y):
    if x+2<N and y+1<M:
        return arr[x][y]+arr[x+1][y]+arr[x+2][y]+arr[x+1][y+1]
    return 0

def f(x,y):
    if x+2<N and y+1<M:
        return arr[x][y]+arr[x+1][y]+arr[x+2][y]+arr[x+2][y+1]
    return 0

def g(x,y):
    if x+2<N and y+1<M:
        return arr[x][y]+arr[x][y+1]+arr[x+1][y+1]+arr[x+2][y+1]
    return 0

def h(x,y):
    if x+2<N and y+1<M:
        return arr[x+1][y]+arr[x][y+1]+arr[x+1][y+1]+arr[x+2][y+1]
    return 0

def i(x,y):
    if x+2<N and y+1<M:
        return arr[x+2][y]+arr[x][y+1]+arr[x+1][y+1]+arr[x+2][y+1]
    return 0

def j(x,y):
    if x+2<N and y+1<M:
        return arr[x][y]+arr[x+1][y]+arr[x+1][y+1]+arr[x+2][y+1]
    return 0

def k(x,y):
    if x+2<N and y+1<M:
        return arr[x+1][y]+arr[x][y+1]+arr[x+1][y+1]+arr[x+2][y]
    return 0

def l(x,y):
    if x+1<N and y+2<M:
        return arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y]
    return 0

def m(x,y):
    if x+1<N and y+2<M:
        return arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]
    return 0

def n(x,y):
    if x+1<N and y+2<M:
        return arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+2]
    return 0


def o(x,y):
    if x+1<N and y+2<M:
        return arr[x+1][y]+arr[x+1][y+1]+arr[x+1][y+2]+arr[x][y]
    return 0

def p(x,y):
    if x+1<N and y+2<M:
        return arr[x+1][y]+arr[x+1][y+1]+arr[x+1][y+2]+arr[x][y+1]
    return 0

def q(x,y):
    if x+1<N and y+2<M:
        return arr[x+1][y]+arr[x+1][y+1]+arr[x+1][y+2]+arr[x][y+2]
    return 0

def r(x,y):
    if x+1<N and y+2<M:
        return arr[x+1][y]+arr[x+1][y+1]+arr[x][y+1]+arr[x][y+2]
    return 0

def s(x,y):
    if x+1<N and y+2<M:
        return arr[x][y]+arr[x+1][y+1]+arr[x][y+1]+arr[x+1][y+2]
    return 0


re =0
for AA in range(N):
    for BB in range(M):
        tmp = max(a(AA,BB),b(AA,BB),c(AA,BB),d(AA,BB),e(AA,BB),f(AA,BB),g(AA,BB),h(AA,BB),i(AA,BB),j(AA,BB),k(AA,BB),l(AA,BB),m(AA,BB),n(AA,BB),o(AA,BB),p(AA,BB),q(AA,BB),r(AA,BB),s(AA,BB))
        if re < tmp:
            re = tmp

print(re)

