a = int(input())
dat = list(map(int, input().split()))
li =[[dat[0], 1]]
for i in dat[1:]:
    if li[-1][0] != i:
        li.append([i, 1])
    else:
        li[-1][1] +=1

re=0
b=0
c=0
le =[]
i=0

def back(i):
    now = li[i][0]
    while i>=0:
        if li[i][0] == now:
            i-=1
        else:
            return i

while i< len(li):
    if b ==0:
        b = li[i][0]
        re+= li[i][1]
        i+=1
        continue    
    if c ==0:
        c =  li[i][0]
        re+= li[i][1]
        i+=1
        continue
    if  li[i][0] ==b or li[i][0] ==c:
        re+= li[i][1]
        i+=1
        continue
    i = back(i-1)+1
    b=0
    c=0
    le.append(re)
    re=0

le.append(re)

print(max(le))