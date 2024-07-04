import sys
a = int(input())
li = [0 for i in range(10000)]
for i in range(a):
  b = int(sys.stdin.readline())
  li[b-1]+=1

for i in range(10000):
  for j in range(li[i]):
    print(i+1)









# dic ={}
# for i in range(a):
#   b = int(sys.stdin.readline())
#   if b in dic:
#     dic[b]+=1
#   else:
#     dic[b]=1

# dic = dict(sorted(dic.items()))
# for key, value in dic.items():
#   print(f'{key}\n'*value, end="")