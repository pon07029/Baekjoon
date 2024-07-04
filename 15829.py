def ser(n):
  tmp = 0
  x = 1
  while tmp != n:
    tmp +=1
    x *=31
    if x > 1234567891:
      x = x%1234567891
  return x

a = int(input())
b = input()
sum =0
for i in range(len(b)):
  sum +=(ord(b[i])-96)*ser(i)

print(sum%1234567891)
