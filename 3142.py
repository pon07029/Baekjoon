import sys
input=sys.stdin.readline
N=int(input())
n=1000000
s=[False]*(n+1)
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

c=0
for i in range(N):
    x=int(input())
    if x==1:
        print("NE" if c else "DA")
    if a[x]:
        if s[x]:
            s[x]=False
            c-=1
        else:
            s[x]=True
            c+=1
        print("NE" if c else "DA")
        continue
    while x>1:
        for j in primes:
            if x%j==0:
                if s[j]:
                    s[j]=False
                    c-=1
                else:
                    s[j]=True
                    c+=1
                x//=j
                break
    print("NE" if c else "DA")
    

