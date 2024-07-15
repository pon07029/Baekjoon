N, S, M =map(int, input().split())
dat = list(map(int, input().split()))
tmp =[S]

for i in range(1,N+1):
    t= []
    for j in tmp:
        if j+dat[i-1]<=M:
            t.append(j+dat[i-1])
        if j-dat[i-1]>=0:
            t.append(j-dat[i-1])
    tmp = list(set(t))
    if not tmp:
        print(-1)
        exit()

print(max(tmp))
    