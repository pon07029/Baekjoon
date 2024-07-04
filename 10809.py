b = "abcdefghijklmnopqrstuvwxyz"
a = input()
re = ""
for i in b:
  re += f"{a.find(i)} "

print(re)