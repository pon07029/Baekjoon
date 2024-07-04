
re=[]
for i in range(10):
  b = int(input())
  re.append(b%42)

print(len(list(set(re))))