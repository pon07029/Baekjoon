import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))
n=100000
ff = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if ff[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        ff[j] = False
fin=False
def sol():
    global fin
    a,b=map(int,input().split())
    if a==0 and b==0:
        exit()
    co=b-a+1
    num=[i for i in range(a,b+1)]
    li=[]
    for i in num:
        tmp=[]
        c=0
        for j in primes:
            if i%j==0:
                tmp.append(j)
                c+=1
            if c>=co:
                break
            if j>i:
                break
        li.append(tmp)

    fin=False

    def f(arr,l):
        global fin
        se=set(arr)
        if fin:
            return
        if l==co:
            print(*arr)
            fin=True
            return
        for i in li[l]:
            if i not in se:
                f(arr+[i],l+1)
    
    f([],0)
while 1:
    sol()
