n=int(input())
li = list(map(int, input().split()))
le =[0]*n
la =[0]*n
la[-1]=1
le[0]=1

def f(length):
    mx=0
    for i in range(length):
        if li[i]<li[length]:
            mx=max(mx,le[i])
            # print(i,length, li[i],li[length], le[i], mx)
    if mx==0:
        return 1
    else:
        return mx+1
    
def ff(length):
    mx=0
    for i in range(length+1,n):
        if li[i]<li[length]:
            mx=max(mx,la[i])
    if mx==0:
        return 1
    else:
        return mx+1       

for i in range(1,n):

    le[i]=f(i)
for i in range(n-2,-1, -1):
    la[i]=ff(i)
mxx=0
for i in range(n):
    mxx=max(mxx,le[i]+la[i]-1)
print(mxx)
