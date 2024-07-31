N = int(input())
li = []
mod=[]
lenth=[0]*N
lenn=[0]*(2**N)

for _ in range(N):
    p=int(input())
    li.append(p)
    while p>0:
        lenth[_]+=1
        p//=10
    lenn[1<<_]=lenth[_]
K=int(input())
print(lenn)
print(lenth)
def ff(v, vi):
    if vi==(1<<N)-1:
        return v
    for i in range(N):
        if vi & (1 << i):
            continue
        lenn[vi | (1 << i)]= v+lenth[i]
        ff(v+lenth[i], vi | (1 << i))

for i in range(N):
    mod.append(li[i] % K)
dp={}

def f(mo, vi):
    if vi == 0:
        if mo % K == 0:
            return 1
        else:
            return 0
      
    if (mo, vi) in dp:
        return dp[(mo, vi)] 
    modsum=0
    for next in range(N):
        if vi & ~(1 << next):
            len = 0
            for i in range(lenth[next]):
                len = len * 10 + 1
                len %= K
    dp[(mo, vi)] = modsum
    return modsum 

print(f(0, (1 << N) - 1))
