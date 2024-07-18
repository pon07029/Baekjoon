N=int(input())
dat= list(map(int, input().split()))
b= max(dat)
le=[False]*(b+1)
for i in dat:
    le[i]=True

re=[0]*(b+1)
for i in dat:
    for j in range(i*2, b+1, i):
        if le[j]:
            re[j]-=1
            re[i]+=1
for i in dat:
    print(re[i], end=' ')