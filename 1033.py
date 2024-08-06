N=int(input())
tmp=[]

def f(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(N-1):
    a,b,c,d=map(int,input().split())
    li=[0]*N
    gcd=f(c,d)
    li[a]=c//gcd
    li[b]=d//gcd
    tmp.append(li)
if N==1:
    print(1)
    exit()

re=tmp.pop()
while len(tmp)>0:
    k=1
    li=tmp.pop()
    for i in range(N):
        if re[i] and li[i]:
            gcd=f(re[i],li[i])
            a=re[i]//gcd
            b=li[i]//gcd
            for i in range(N):
                re[i]*=b
                li[i]*=a
            for i in range(N):
                if li[i]:
                    re[i]=li[i]
            k=0
            break
    if k:
        tmp.append(li)
    
print(*re)