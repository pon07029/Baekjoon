
d = int(input())
sum =0
a = int(input())
for i in range(a):
  c, b= map(int, input().split())
  sum += c*b

print("Yes" if sum == d else "No")