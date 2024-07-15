import sys
input = sys.stdin.readline

M = 1000000007
def f(a,x):
  if x == 1:
    return a
  d = f(a,x//2)
  if x%2 == 0:
    return d*d%M
  else:
    return d*d*a%M

count = 0
for i in range(int(input())):
  a,b = map(int,input().split())
  c = f(a,M-2)
  count = (count + c*b%M)%M

print(count)