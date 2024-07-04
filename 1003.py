def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return [a, b]

li = []

for i in range(int(input())):
  a= int(input())
  k =fibo(a-1)
  if a==0:
    k.reverse()
  
  li.append(k)

for i in li:
   print(i[0], i[1])