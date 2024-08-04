import math
arr=[0]*10000
su=[-1]*10000
arr[0]=2
su[0]=2
N=int(input())
li=[]
for i in range(N):
    li.append(int(input()))
     

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
for i in range(1,10000):
    arr[i]=f(i+1)
for i in range(1,10000):
    su[i]=su[i-1]+arr[i]
for i in li:
    print(su[i-1])
