import sys
input=sys.stdin.readline
V, E=map(int,input().split())
p=[i for i in range(V+1)]
edges=[]
re=0
for _ in range(E):
    a,b=map(int,input().split())
    edges.append((a,b))

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

for edge in edges:
    re+=1
    a,b=edge
    if fp(a)!=fp(b):
        up(a,b)
    else:
        print(re)
        exit(0)
print(0)