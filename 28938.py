b = int(input())
dat = list(map(int, input().split()))
a=0
for i in dat:
  a+=i

if a == 0:
    print("Stay")
elif a >0:
    print("Right")
else:
    print("Left")