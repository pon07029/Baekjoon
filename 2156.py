import sys
n = int(input())

if n==1:
    print(input())
    sys.exit()

li = [0]
li.append([int(input())])
x=int(input())
li.append([0,li[1][0]+x, x])
for _ in range(2, n):
    x = int(input())
    li.append([max(li[-1]),x+li[-1][2], x+max(li[-2])])
print(max(max(li[-1]), max(li[-2])))  