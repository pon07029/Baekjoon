a, b= map(int, input().split())

c = list(map(int, input().split()))

sum=[]
for i in c:
  if i < b:
    sum.append(i)
print(" ".join(map(str, sum)))
