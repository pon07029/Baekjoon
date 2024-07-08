N, K =map(int, input().split())
li=[999999]*(K+3)

if N>=K:
    print(N-K)
    exit()
q=[]
if N==0:
    li[1]=1
    q.append(1)
else:
    q.append(N)
    li[N]=0


while q:
    tmp=[]
    for i in q:
        if i==K:
            print(li[i])
            break
        if i-1> 0:
            if li[i-1]>li[i]+1:
                li[i-1]=li[i]+1
                tmp.append(i-1)
        if i+1<=K:
            if li[i+1]>li[i]+1:
                li[i+1]=li[i]+1
                tmp.append(i+1)
        if i*2<=K+1:
            if li[i*2]>li[i]:
                li[i*2]=li[i]
                tmp.append(i*2)
    q=tmp


