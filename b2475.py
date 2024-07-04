dat = list(map(int, input().split()))
sum =0
for i in dat:
  sum+=i*i

print(sum%10)