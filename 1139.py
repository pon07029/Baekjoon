N =int(input())
li=list(map(int,input().split()))
tr=[[[0 for i in range(N)]for j in range(N)]for k in range(N)]
li.sort()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            a,b,c=li[i],li[j],li[k]
            if a<=b<=c and a+b>c:
                p=(a+b+c)/2
                tr[i][j][k]=(p*(p-a)*(p-b)*(p-c))**0.5
dp = {}

def ff(c):
    t=0
    for i in range(N):
        if c & (1 << i):
            t+=1
    return N-t

def f(vi):
    if ff(vi)<3:
        return 0
    if vi in dp:
        return dp[vi] 
    mi = 0
    for i in range(N):
        if vi & (1 << i):
            continue
        for j in range(i,N):
            if vi & (1 << j):
                continue
            for k in range(j,N):
                if vi & (1 << k):
                    continue
                # print( tr[i][j][k])
                mi = max(mi, f(vi | (1 << i) | (1 << j) | (1 << k)) + tr[i][j][k])

    dp[vi] = mi 
    return mi  
print(f(0))