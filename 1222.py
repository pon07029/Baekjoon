import math
N=int(input())
li=list(map(int,input().split()))
re=[0]*2000000
def f(x):

            for i in range(1, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    re[i]+=1
                    if ( (i**2) != x) : 
                        re[(x // i)]+=1
            
for i in li:
    f(i)

print(re[:10])