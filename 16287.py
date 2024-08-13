w,n=map(int, input().split())
arr=list(map(int, input().split()))
def f():
    ar1=[0]*(w+1)
    for i in range(n):
        for j in range(i+1,n):
            nw=arr[i]+arr[j]
            if nw<=w:
                ar1[nw]=(i,j)
    for i in range(n):
        for j in range(i+1,n):
            nw=arr[i]+arr[j]
            if nw<=w:
                if ar1[w-nw] and i not in ar1[w-nw] and j not in ar1[w-nw]:
                    print('YES')
                    exit()
    print('NO')
f()
