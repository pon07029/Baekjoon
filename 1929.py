#소수
a, b= map(int, input().split())

re = [2]
for i in range(3, b+1):

  for j in re:
    if i %j ==0:
      break 
    if j > i**0.5:
      if re[-1] <i:
        re.append(i)
      break

for i in re:
  if i>=a:
    print(i)