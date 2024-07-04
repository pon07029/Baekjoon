re=[]
for i in range(int(input())):
  a= input()
  re.append(a)

le =list(re[0])
b = len(re[0])
for i in range(b):
  for j in re:
    if j[i] != le[i]:
      le[i] = "?"
      break
print(''.join(le))

