re = []

dat = list(map(int, input().split()))

for i in dat:
  if i>1:
    re.append(1)

print("S" if len(re)==0 else "F")

