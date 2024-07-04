k = int(input())
re = []
for i in range(k):
  j = input()
  re.append(j[0]+j[len(j)-1])

for i in re:
  print(i)