import sys
input=  sys.stdin.readline
def f(num, n, now):
    if len(str(num)) ==n-1:
        return now
    for i in range(10):
        k = int(str(i)+now)**3
        if num%(10**n) == k%(10**n):
            return f(num, n+1, str(i)+now)            
for i in range(int(input())):
  a= int(input())
  print(int(f(a,1,"")))