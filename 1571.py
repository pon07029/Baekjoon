import math
N=int(input())
li=[]
for i in range(N):
    li.append(input())
w=input()
l=[0]*27
for i in range(len(w)):
    le=len(li[i])
    if l[le]==0:
        l[le]=li[i].find(w[i])+1
        if l[le]==0:
            print(-1)
            exit()
    else:
        if l[le]!=li[i].find(w[i])+1:
            print(-1)
            exit()
        if li[i].find(w[i])==-1:
            print(-1)
            exit()

a1,a2=1,1
for i in range(1,27):
    if l[i]==0:
        continue
    b1,b2=i,l[i]
    gcd=math.gcd(a1,b1)
    if b2%gcd!=a2%gcd:
        print(-1)
        exit()
    lcm=a1*b1//gcd
    for j in range(lcm//a1+2):
        if (j*a1+a2)%b1==b2%b1:
            a2=j*a1+a2
            a1=lcm
            break
print(a2-1)