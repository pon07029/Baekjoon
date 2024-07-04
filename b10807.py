a= int(input())
b = list(map(int, input().split()))
c= int(input())
sum=0
for i in b:
  if i==c:
    sum+=1
print(sum)
