
import math
N=int(input())

if N==1:
    print(0)
    exit()
if N==2:
    print(1)
    exit()
if N==3:
    print(1)
    exit()

def is_prime_number(n):
    array = [True for i in range(n+1)] 

    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]
primes=is_prime_number(N)
l= len(primes)
kk=0
for i in range(l):
   tmp=0
   for j in range(i,l):
        tmp+=primes[j]
        if tmp==N:
            kk+=1
            break
        if tmp>N:
            break
print(kk)