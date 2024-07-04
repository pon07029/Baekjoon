import sys
z= int(sys.stdin.readline())
dat = list(map(int, sys.stdin.readline().split()))
print(max(dat)*min(dat))