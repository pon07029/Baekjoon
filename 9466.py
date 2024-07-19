import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def f():
    c=0
    N= int(input())
    dat=list(map(int, input().split()))
    ch=[True]*(N+1)

    def ff(a,arr):
        global c
        if ch[a]:
            arr.append(a)
            ch[a]=False
            ff(dat[a-1],arr)
        else:
            for i in arr:
                if i==a:
                    return
                c+=1
            return
    for i in range(1,N+1):
        if ch[i]:
            ff(i,[])

for _ in range(int(input())):
    c=0
    f()
    print(c)

