a, b= map(int, input().split())
dat = list(map(int, input().split()))
li=[]
l = len(dat)
for i in range(l):
  for j in range(l):
    for k in range(l):
      if i != j and j != k and k != i and dat[i]+dat[j] + dat[k] <= b:
        li.append(dat[i]+dat[j] + dat[k])

print(max(li))