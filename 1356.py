def fun(a):
  sum=1
  for i in a:
    sum*=int(i)
  return sum

a = input()
k ="NO"
for i in range(1, len(a)):
  if fun(a[:i]) == fun(a[i:]):
    k="YES"
    break
print(k)