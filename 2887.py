import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    a,b,c=map(int,input().split())
    li.append((a,b,c,i+1))


p=[i for i in range(N+1)]
edges=[]
li.sort(key=lambda x:x[0])
for i in range(N-1):
    edges.append((li[i+1][0]-li[i][0],li[i][3],li[i+1][3]))
li.sort(key=lambda x:x[1])
for i in range(N-1):
    edges.append((li[i+1][1]-li[i][1],li[i][3],li[i+1][3]))
li.sort(key=lambda x:x[2])
for i in range(N-1):
    edges.append((li[i+1][2]-li[i][2],li[i][3],li[i+1][3]))

re=0

edges.sort()

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
    c,a,b=edge
    if fp(a)!=fp(b):
        up(a,b)
        re+=c
print(re)
