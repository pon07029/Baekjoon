import sys
arr=[]
def f(N,n):
    if n==1:
        
        return [1, 0] if arr[N[0]][N[1]] ==0 else [0, 1]
    now = arr[N[0]][N[1]]
    for i in range(N[0], N[0]+n):
        for j in range(N[1], N[1]+n):
            if now != arr[i][j]:
                a=f([N[0], N[1]], n//2)
                b=f([N[0]+n//2, N[1]], n//2)
                c=f([N[0], N[1]+n//2], n//2)
                d=f([N[0]+n//2, N[1]+n//2], n//2)
                return [a[0]+b[0]+c[0]+d[0], a[1]+b[1]+c[1]+d[1]]
    return [1, 0] if now == 0 else [0, 1]

a = int(input())
for _ in range(a):
    arr.append(list(map(int, sys.stdin.readline().split())))
print(*f([0, 0], a), sep='\n')