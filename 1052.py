N,K=map(int,input().split())
c=0

while bin(N).count('1')>K:
    k=bin(N)[::-1].index("1")
    c+=2**k
    N+=2**k
print(c)