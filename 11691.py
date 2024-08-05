import math
import copy
li=[]
li.append({})
c=[1]
n=int(input())
re=[0]*n
ll=[0]
res=[0]
def f(x):
    g={}
    re=1
    r2=1
    while x != 1:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    g=li[x//i-1].copy()
                    if i in g:
                        g[i] += 1
                    else:
                        g[i] = 1
                    x=1
                    break
            if x>1:
                if x in g:
                    g[x] += 1
                else:
                    g[x] = 1
                    break
    li.append(g)
    for k, v in g.items():
        re *= (k ** v //k*(k-1))
        r2 *= (k ** (v+1)-1)//(k-1)
    c.append(re)
    ll.append(r2)
for i in range(n-1):
    f(i+2)
for i in range(1,n):
    res.append(c[i]*(i+1)+ll[i])

print(li)
print(ll)
print(c)
