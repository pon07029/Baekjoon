li=[]
N=int(input())
li.append(0)
for i in range(1,12):
    li.append(i*(10**(i-1)))
total=[0]*10
cu=0
def co(n):
    global cu
    l=len(str(n))
    cu+=(n-(10**(l-1))+1)*l
    for i in range(1,l):
        cu+=i*9*(10**(i-1))

def ff(c,le):
    for i in range(1,10):
        total[i]+=c*li[le]

def f(num):
    l=len(str(num))
    if l==1:
        for i in range(1,num+1):
            total[i]+=1
        return
    fi=int(str(num)[0])
    for i in range(1,fi):
        total[i]+=10**(l-1)
    ff(fi,l-1)
    total[fi]+=int(str(num)[1:]) + 1
    f(int(str(num)[1:]))
f(N)
co(N)
total[0]=cu-sum(total)
print(*total)