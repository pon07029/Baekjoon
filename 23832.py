import math
N=int(input())

arr=[0]*N
su=[-1]*N
arr[0]=2
su[0]=2
   

def f(x):
    k=x
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
for i in range(1,N):
    arr[i]=f(i+1)
for i in range(1,N):
    su[i]=su[i-1]+arr[i]

print(su[N-1]-2)
