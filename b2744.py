s = input()
sum = ""
for i in range(len(s)):
  if(s[i].islower()):
    sum+=s[i].upper()
  else:
    sum+=s[i].lower()

print(sum)