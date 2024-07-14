an=""
li=[]
for i in input():
    if i=="(":
      li.append(i)
    elif i==")":
      while li and li[-1]!="(":
         an+=li.pop()
      li.pop()
    elif i in "+-":
      while li and li[-1]!="(":
         an+=li.pop()
      li.append(i)
    elif i in "*/":
      while li and li[-1] in "*/":
         an+=li.pop()
      li.append(i)
    else:
      an+=i
while li:
    an += li.pop()
print(an)