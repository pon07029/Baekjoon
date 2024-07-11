x, y = map(int, input().split())
li= [9999] * 100001
if x>=y:
    print(x-y)
    print(1)
    exit()
q=[x]
c=0
while q:
    tmp=[]
    ti=0
    for i in q:
        if i==y:
            ti+=1
        if i*2<=100000 and li[i*2]>=c:
            li[i*2]=c
            tmp.append(i*2)
        if i+1<=100000 and li[i+1]>=c:
            li[i+1]=c
            tmp.append(i+1)
        if i-1>=0 and li[i-1]>=c:
            li[i-1]=c
            tmp.append(i-1)
    if ti:
        print(c)
        print(ti)
    c+=1
    q=tmp
        