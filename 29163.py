c = int(input())
dat = list(map(int, input().split()))

b = 0
for i in dat:
  b+=i%2

print("Happy" if (c-b-b) >0 else "Sad")