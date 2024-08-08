import math
N,M=map(int,input().split())
t=math.comb((N+1)*(M+1),3)
if N>1:
    t-=(M+1)*math.comb(N+1,3)
if M>1:
    t-=(N+1)*math.comb(M+1,3) 

for i in range(2,N+1):
    for j in range(2,M+1):
        gcd=math.gcd(i,j)
        if gcd-1:
            t-=2*(N-i+1)*(M-j+1)*(gcd-1)

print(t)