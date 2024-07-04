import sys
a = int(input())
sum=0
for i in range(a):
    b = int(sys.stdin.readline())
    sum+=b

print(sum-a+1)