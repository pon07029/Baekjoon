import math
a,b=map(int,input().split())
n=int(math.sqrt(b))
ff = [False,False] + [True]*(n-1)
primes=[]
zi=[]
for i in range(2,n+1):
  if ff[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        ff[j] = False
for i in primes:
    zi.append(i*i)
li=[1]*(b+1-a)
for i in zi:
    st=a//i
    st*=i
    if st<a:
        st+=i
    for j in range(st,b+1,i):
        li[j-a]=0
print(li.count(1))
