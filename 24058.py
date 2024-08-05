import math
n,k =map(int,input().split())
re=1
c=1

if n==1:
    print(k*(k+1)//2)
    exit()

def f(p):
    x=p
    global re
    global c
    g={}
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
       c*=(v+1)
    return re
print((f(n)*n//2)*k+(k-1)*(k)//2*n*c)
