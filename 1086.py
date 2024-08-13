import sys
import math
input=  sys.stdin.readline
N = int(input())
li = []
lent = [0]*N
sm=[0]*N
for i in range(N):
    li.append(int(input()))
    lent[i] = len(str(li[i]))
K = int(input())

mod=[]
for i in range(N):
    sm[i]=li[i]%K

for i in range(52):
    mod.append(10**i % K)
dp = {}
def f(vi):
    if vi in dp:
        return dp[vi]
    tmp=[0]*K
    for next in range(N):
        if vi & (1 << next):
            tp=f(vi ^ (1 << next))
            for i in range(K):
                na=(mod[lent[next]]*i+sm[next])%K
                tmp[na]+=tp[i]
    dp[vi]=tmp
    return dp[vi]
for i in range(N):
    dp[1 << i]=[0]*K
    dp[1 << i][li[i]%K]=1
f((1 << N)-1)
li=[i+1 for i in range(N)]
kkk=1
re=dp[(1 << N)-1][0]
for i in li:
    if re%i==0:
        re//=i
    else:
        kkk*=i
gcd=math.gcd(re,kkk)
print(f"{re//gcd}/{kkk//gcd}")