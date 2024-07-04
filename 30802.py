import math
a = int(input())
dat = list(map(int, input().split()))
b, c= map(int, input().split())
sum =0
for i in dat:
  sum+=math.ceil(i/b)
print(sum)
print(f"{a//c} {a%c}")