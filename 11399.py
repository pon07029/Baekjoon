import sys
a = int(input())
dat = list(map(int, sys.stdin.readline().split()))  
dat.sort()
sum=0
for i in range(a):
    sum+=dat[i]*(a-i)
print(sum)