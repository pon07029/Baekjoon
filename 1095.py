S,F,M = map(int,input().split())
so={}
arr = [i for i in range(M+1)] 
def f(na):
    global S,F
    a=S+F
    ss=S
    ff=F
    cnt=0
    while a>1:
        a//=na
        cnt+=a
    while ss>1:
        ss//=na
        cnt-=ss
    while ff>1:
        ff//=na
        cnt-=ff
    return cnt

def prime_numbers(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == i: 
            for j in range(i*i, n+1, i): 
                if arr[j]==j:
                    arr[j]=i
    return [i for i in range(2,n+1) if arr[i]==i]
sosu=prime_numbers(M)
for i in sosu:
    so[i]=f(i)

for i in range(M,1,-1):
    g={}
    nn=i
    while nn>1:
        if arr[nn] in g:
            g[arr[nn]]+=1
        else:
            g[arr[nn]]=1
        nn//=arr[nn]
    tmp=True
    for k, v in g.items():
        if not k in so:
            tmp=False
            break
        else:
            if so[k]<v:
                tmp=False
                break
    if tmp:
        print(i)
        exit()
print(1)