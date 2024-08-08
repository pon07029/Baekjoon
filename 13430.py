import math
k,n=map(int,input().split())
re=math.comb(n+k,k+1)%1000000007
print(re)