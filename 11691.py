import math
N=int(input())
pi=[0]*(N+1)
pp=0

def sieveOfEratosthenes(N):
    prime_list=set(range(2, N+1)) # 2부터 N을 갖는 집합 자료형 선언
    for i in range(2, N+1): # 2부터 N까지 반복
        if i in prime_list: 
            prime_list -= set(range(2*i, N+1, i)) # 차집합 연산을 통해 자신을 제외한 소수의 배수 제거
    return prime_list

for i in sieveOfEratosthenes(N):
    pi[i]=i-1

            

def ff(x):
    g={}
    re=1
    while x != 1:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    x = x // i
                    if i in g:
                        g[i] += 1
                    else:
                        g[i] = 1
                    break
            else:
                if x in g:
                        g[x] += 1
                else:
                        g[x] = 1
                break
    for k, v in g.items():
        re *= (k ** v //k*(k-1))
    return re


def f(x):
    if pi[x]:
        return
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if math.gcd(i,x//i)==1:
              pi[x]=pi[i]*pi[x//i]
              return
    pi[x]=ff(x)

for i in range(2,N+1):
    f(i)
for i in range(2,N+1):
     t=N//i
     k=t*(t+1)//2
     p=(pi[i]*i*i)//2
     pp+=k*p
     pp%=1000000007
print(pp)
# print(pi)