import sys
a, b = map(int, sys.stdin.readline().split())
li = []
sum=0
for i in range(a):
    li.append(int(sys.stdin.readline()))

for i in li[::-1]:
    if b >= i:
        sum+= b//i
        b = b%i

print(sum)