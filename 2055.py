import math
N,M=map(int,input().split())
t=math.comb((N+1)*(M+1),3)
if N>1:
    t-=(M+1)*math.comb(N+1,3)
if M>1:
    t-=(N+1)*math.comb(M+1,3) 
for i in range(1,N//2+1):
    k=N//i
    p=N%i+1
    if M>=k:
        t-=p*(M-k+1)*math.comb(k+1,3)*2
for i in range(1,M//2+1):
    k=M//i
    p=M%i+1
    if N>=k:
        t-=p*(N-k+1)*math.comb(k+1,3)*2
s=min(N,M)
t+=math.comb(s+1,3)*2
print(t)