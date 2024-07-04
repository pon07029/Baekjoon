def fun(a):
  if a== 1:
    return 0
  if a == 2 or a ==3:
    return 1
  i=2
  while i * i <= a:
        if a % i == 0 or a % (i + 1) == 0:
            return 0
        i += 1
  return 1

a = int(input())
dat = list(map(int, input().split()))
re =0
for i in dat:
  re += fun(i)
print(re)
