dic={}
a = input().lower()
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

big = max(list(dic.values()))
li=[]
for key, value in dic.items():
    if value == big:
        li.append(key)
if len(li) ==1:
  for key, value in dic.items():
    if value == big:
        print(key.upper())
else:
    print("?")