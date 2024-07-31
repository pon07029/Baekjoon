import sys
input=sys.stdin.readline
G=int(input())
P=int(input())
li=[0]*P
p=[i for i in range(G+1)]
for i in range(P):
    li[i]=int(input())
c=0
def fp(x):
    if p[x]==x:
        return x
    p[x]=fp(p[x])
    return p[x]

def up(a,b):
    a=fp(a)
    b=fp(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

for i in li:
    a= fp(i)
    if a==0:
        break
    if fp(i)!=a:
        up(a,i)
    else:
        up(i,a-1)
    c+=1
    # print(p)
print(c)
