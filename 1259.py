def fun(a):
  
  for i in range(len(a)//2):
    if a[i] != a[len(a)-i-1]:
      return "no"
  
  return "yes"

re = []
while True:
    a = input()

    if a=="0":
        break

    re.append(a)

for i in re:
  print(fun(i))