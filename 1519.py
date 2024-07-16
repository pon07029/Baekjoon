N=int(input())
def f(n):
    dat = list(str(n))
    l=len(dat)
    tmp=[]
    for i in range(l):
        for j in range(i+1,l+1):
            k= int(''.join(dat[i:j]))
            if k!=0 and k!= n:
                tmp.append(k)
    tmp.sort()
    # print(tmp, n,"입니다")
    return tmp
li=[-1]*(N+1)
if N<10:
    print(-1)
    exit()
li[10]=1
for i in range(10,N+1):
    for j in f(i):
        if li[i-j]==-1:
            li[i]=j
            break
# print(*li)
print(li[N])

    