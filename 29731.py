a = int(input())
c = ["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

re=[]
for i in range(a):
  b = input()
  if b not in c:
    re.append(b)

print("Yes" if len(re)>0 else "No")
