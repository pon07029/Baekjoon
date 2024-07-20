import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N= int(input())
M= int(input())
li=[]
for i in range(M):
    a,b,c=map(int, input().split())
    li.append((a,b,c))
g={}
g[N]=[]
while li:
    tmp=[]
    for a,b,c in li:
        if a in g:
            g[a].append((b,c))
            if not b in g:
                g[b]=[]
        else:
            tmp.append((a,b,c))
    
    li=tmp
re=[[0 for i in range(N+1)]for j in range(N+1)]
ch=[False]*(N+1)

for i in range(1,N+1):
    if g[i]:
        continue
    ch[i]=True
    re[i][i]=1

def ff(k,c):
    if ch[k]:
        return [num*c for num in re[k]]
    tm=[0]*(N+1)
    ch[k]=True
    for i,cc in g[k]:
        arr=ff(i, cc)
        tm = [tm[j]+ arr[j] for j in range(N+1)]
    re[k]=tm
    return [num*c for num in tm]

# print(ff(N,1))
kkk=ff(N,1)
for i in range(1,N+1):
    if kkk[i]:
        print(i, kkk[i])
