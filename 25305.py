import sys
a, b = map(int, sys.stdin.readline().split())
dat = list(map(int, sys.stdin.readline().split()))  

dat.sort(reverse=True)

print(dat[b-1])