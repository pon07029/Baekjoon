import itertools

c=[]
h=[]
a, b= map(int, input().split())
for i in range(a):
    dat = list(map(int, input().split()))
    for j in range(len(dat)):
        if dat[j]==1:
            h.append([i,j])
        if dat[j]==2:
            c.append([i,j])
ch=[]
for i in range(len(c)):
    tmp=[]
    for j in range(len(h)):
        tmp.append(abs(c[i][0]-h[j][0])+abs(c[i][1]-h[j][1]))
    ch.append(tmp)

def csum(arr,n):
    
    s=0
    for i in range(len(h)):
        s+=min(arr[j][i] for j in range(len(arr)))
    return s

elements = list(range(len(c)))
combinations = list(itertools.combinations(elements, b))
minn=999999999
for comb in combinations:
    selected_elements = [ch[i] for i in comb]
    minn=min(minn,csum(selected_elements,len(h)))

print(minn)
